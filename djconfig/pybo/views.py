from django.shortcuts import render

from django.http import HttpResponse


def main(request):
    return render(request, 'base.html')


# Create your views here.
