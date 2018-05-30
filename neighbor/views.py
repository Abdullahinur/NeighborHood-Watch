from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from neighbor.forms import SignupForm, UserProfileForm, NeighborhoodForm, PostForm, BusinessForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from neighbor.tokens import account_activation_token
from django.contrib.auth.models import User
from neighbor.models import Neighborhood, UserProfile, Business, Post
from django.core.mail import EmailMessage
from django.views.decorators.http import require_POST
from itertools import chain

'''
Function to return confirm message
'''


def confirm(request):
    return render(request, 'registration/confirm.html')


'''
Function to signup
'''


def signup(request):
    if request.method == 'POST':
        user_form = SignupForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
                email.send()
                return redirect('confirm')
            else:
                profile.save()
                email.send()
                registered = True
                return redirect('confirm')

    else:
        user_form = SignupForm()
        profile_form = UserProfileForm(data = request.POST)
    return render(request, 'registration/signup.html', {'user_form': user_form, 'profile_form': profile_form,})


'''
Function to send activate the account
'''


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        return render(request, 'registration/success.html')
    else:
        return HttpResponse('Activation link is invalid!')


'''
Function to login the User
'''


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user:
                login(request, user)
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)

            else:
                return HttpResponse("Your account is disabled.")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'registration/invalid.html')

    else:

        return render(request, 'registration/login.html')


'''
Function to create neighborhood
'''


@login_required
def create_neighborhood(request):
    form = NeighborhoodForm()
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = Neighborhood(image = request.FILES['image'])
            neighborhood = form.save(commit=True)
            return redirect('neighborhoods')
    else:
        print(form.errors)
    return render(request, 'neighborhood/neighborhood.html', context = {'form':form,})


'''
Function to display neighborhoods
'''


@login_required
def neighborhoods(request):
    neighborhoods = Neighborhood.objects.all()
    return render(request, 'neighborhood/neighborhood_view.html', context = {'neighborhoods' : neighborhoods,})


'''
Function to edit neighborhoods
'''


@login_required
def show_neighborhood(request, id=None):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    form = BusinessForm()
    all_businesses = Business.objects.all()
    businesses = all_businesses.filter(neighborhood_id=id)
    print(businesses)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = Business(image = request.FILES.get('image'))
            business = form.save(commit=False)
            business.neighborhood = neighborhood
            business = business.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = BusinessForm()
    return render(request, 'neighborhood/neighborhood_dash.html', context={'form' : form, 'neighborhood' : neighborhood, 'businesses':businesses})


'''
Function to display businesses
'''


@login_required
def view_business(request):
    business = Business.objects.all()
    return render(request, 'business/view_business.html', context = {'business':business})


'''
Function to display one businesses
'''


def one_business(request, id=None):
    business = get_object_or_404(Business, id=id)
    return render(request, 'business/business_dash.html', context = {'business':business})


'''
Function to add businesses
'''


@login_required
def create_business(request):
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = Business(image=request.FILES.get('image'))
            business = form.save(commit=True)
            return redirect('view_business')
    else:
        print(form.errors)
    return render(request, 'business/create_business.html', context={'form': form})


'''
Function to display the home page
'''


def index(request):
    neighborhoods = Neighborhood.objects.all().order_by('-id')[:4]
    if request.method == 'POST':
        user_form = SignupForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            print('1')

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
                email.send()
            else:
                email.send()
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)

    else:
        user_form = SignupForm()
        profile_form = UserProfileForm(data = request.POST)
        return render(request, 'home/home.html', context = {'neighborhoods' : neighborhoods, 'user_form': user_form, 'profile_form': profile_form,})


'''
Function to logout users
'''


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


'''
Function to display posts
'''


@login_required
def posts(request, id=None):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    form = PostForm()
    all_posts = Post.objects.all().order_by('-id')
    posts = all_posts.filter(neighborhood_id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(image = request.FILES.get('image'))
            post = form.save(commit=False)
            post.author = request.user
            post.neighborhood = neighborhood
            post = post.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = PostForm()
    return render(request, 'posts/posts.html', context = {'form':form, 'posts':posts, 'neighborhood':neighborhood,})


'''
Function to search for neighborhood
'''


def search(request):
    if 'contains' in request.GET and request.GET["contains"]:
            query = request.GET.get("contains")
            businesses = Business.search(query)
            neighborhoods = Neighborhood.search(query)
            results = list(chain(neighborhoods, businesses))


            return render(request, 'registration/search.html',{"output":output, "results":results})

    else:
        message = "You haven't searched for anything"
        return render(request, 'registration/search.html',{"message":message})
    return render(request, 'registration/search.html',)


'''
Function to edit neighborhood
'''


@login_required
def edit_neighborhood(request, id = None):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    n_id = neighborhood.id
    if request.method == 'POST':
        neighborhood.name = request.POST.get('name')
        neighborhood.location = request.POST.get('location')
        neighborhood.population = request.POST.get('population')
        neighborhood.police = request.POST.get('police')
        neighborhood.ambulance = request.POST.get('ambulance')
        if request.FILES == True:
            neighborhood.image = request.FILES.get('image')
            update_neighborhood = neighborhood.save()
            return redirect('show_neighborhood', id=n_id)
        else:
            update_neighborhood = neighborhood.save()
            return redirect('show_neighborhood', id=n_id)
    else:
        return render(request, 'neighborhood/edit_neighborhood.html', {'neighborhood':neighborhood, 'n_id' : n_id,})
    return render(request, 'neighborhood/edit_neighborhood.html', {'neighborhood':neighborhood, 'n_id' : n_id,})


'''
Function to delete neighborhood
'''


@login_required
def delete_neighborhood(request, id = None):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    neighborhood.delete_neighborhood()
    return redirect('neighborhoods')


'''
Function to view user
'''


@login_required
def view_user(request, id = None):
    user = get_object_or_404(User, id=id)
    return render(request, 'home/view_user.html', {'user':user})
