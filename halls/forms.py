from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Video

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", )

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("url", )
        labels = { 'url' : 'YouTube URL' }

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length = 255,
                                  label = 'Search for Videos')
