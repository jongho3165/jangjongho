from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postname', 'contents']
        widgets = {
            'postname': forms.TextInput(attrs={'class': 'form-control'}),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'postname': '제목',
            'contents': '내용',
        }  
