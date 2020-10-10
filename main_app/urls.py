from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user/', views.user, name='user_index'),
    path('user/profile/', views.profile, name='profile'),
    path('cities/index/', views.index, name='index'), 
    path('accounts/signup/', views.signup, name='signup'),
]