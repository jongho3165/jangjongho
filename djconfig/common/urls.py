from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('board/', views.board, name='board'),
    path('board/<int:pk>', views.posting, name='posting'),
    path('board/board_wirte', views.board_wirte, name='board_write')
]