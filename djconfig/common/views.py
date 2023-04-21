from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm
from .models import Post
from .models import Comment
from django.utils import timezone
from .forms import PostForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def board(request):
    postlist = Post.objects.all()
    return render(request, 'common/board.html', { 'postlist':postlist })


def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'common/posting.html', { 'post':post })

def board_wirte(request):
    return render(request, 'common/board_write.html', { 'form':PostForm })
