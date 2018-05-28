from django import forms
from .models import UserProfile, Neighborhood, Business, Post


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('idnumber', 'image')


class PostForm(forms.ModelForm):
    image = forms.FileField(required=False, label='Select an image file', help_text='Please select a photo to upload')
    text_post = forms.CharField(help_text="Please enter some text.")
    class Meta:
        model = Post
        fields = ('image', 'text_post',)
        exclude = ('author',)


class NeighborhoodForm(forms.ModelForm):
    image = forms.FileField(label='Select an image file', help_text='Please select a photo to upload')
    name = forms.CharField(help_text="Please enter the name of the neighborhood.")
    location = forms.CharField(help_text="Please enter the location.")
    population = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    police = forms.CharField(help_text="Please enter the police department phone number.")
    ambulance = forms.CharField(help_text="Please enter the ambulance phone number.")

    class Meta:
        model = Neighborhood
        fields = ('image', 'name', 'location', 'population', 'police', 'ambulance')


class BusinessForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the name of the business.")
    image = forms.FileField(required=False, label='Select an image file', help_text='Please select a photo to upload')
    location = forms.CharField(help_text="Please enter the location of the business.")
    additional_details = forms.CharField(required=False, help_text="Enter any additional details.")

    class Meta:
        model = Business
        fields = ('name', 'image', 'location', 'additional_details',)
        exclude = ('neighborhood',)
