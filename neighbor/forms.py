from django import forms
from .models import UserProfile, Neighborhood, Business, Post


class EditProfileForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'image', 'idnumber', 'neighborhood']


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'image', 'idnumber', 'neighborhood']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'bio', 'image', 'idnumber', 'neighborhood')


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
