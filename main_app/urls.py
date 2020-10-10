from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/<int:user_id>/detail', views.profile_detail, name='profile_detail'),
    path('profile/<int:user_id>/edit', views.profile_edit, name='profile_edit'),
    path('cities/', views.cities_index, name="cities_index"),
    path('cities/<int:city_id>/', views.cities_detail, name='cities_detail'), 
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('accounts/register', views.signup, name='signup'),
    path('accounts/login', views.login, name='login'),
]