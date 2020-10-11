from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:user_id>/edit', views.profile_edit, name='profile_edit'),
    path('cities/', views.cities, name="cities"),
    path('cities/', views.cities_index, name="cities_index"),
    path('cities/<int:city_id>/', views.cities_detail, name='cities_detail'), 
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    url(r'^register/$', views.signup, name='signup'),
]