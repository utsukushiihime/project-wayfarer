from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('profile/', views.profile_detail, name='profile'),
    path('profile/<int:user_id>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:user_id>/delete/', views.profile_delete, name='profile_delete'),
    path('cities/', views.cities_index, name="cities_index"),
    path('cities/<int:city_id>/', views.cities_detail, name='cities_detail'), 
    path('posts/', views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.signup, name='signup'),
]