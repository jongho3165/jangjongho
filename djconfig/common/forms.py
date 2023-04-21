from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'postname', 'contents' ]
        widgets = {
            'contents': SummernoteWidget(),        
        }