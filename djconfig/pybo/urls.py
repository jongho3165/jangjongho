from django.urls import path

from . import views

app_name= 'pybo'

urlpatterns = [
    path('', views.main, name='home'),
    path('board/', views.board, name='board')
]