from django.shortcuts import render

from django.http import HttpResponse


def main(request):
    return render(request, 'base.html')

def board(request):
    return render(request, 'pybo/board.html')
# Create your views here.
