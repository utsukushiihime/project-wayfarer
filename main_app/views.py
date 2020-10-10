from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import City, Post, Profile, Image
from .forms import City_Form, Image_Form, Post_Form, Profile_Form, User_Form, Register_Form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# --- Base Views ---
def home(request):
    return render(request, 'home.html')

def about(request):
    context = {'login': AuthenticationForm(), 'signup': Register_Form()}
    return render(request, 'about.html', context)

def api(request):
    return JsonResponse({"status": 200})

# --- City Index ---
def cities_index(request):
    if request.method == 'POST':
        city_form = City_Form(request.POST)
        if city_form.is_valid():
            new_city = city_form.save(commit=False)
            new_city.user = request.user
            new_city.save()
            return redirect('cities_index')
        cities = City.objects.all()
        city_form = City_Form()
        context = {'cities': cities, 'city_form': city_form, 'login': AuthenticationForm(), 'signup': UserCreationForm()}
        return render(request,'cities/index.html', context)

# --- City Detail ---
def cities_detail(request, city_id):
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city_id=city.id)
    post_form = Post_Form()
    context = {'login': AuthenticationForm(), 'signup': UserCreationForm(), 'city': city, 'post_form': post_form, 'posts': posts}
    return render(request, 'cities/detail', context)
        
# --- Profile Detail ---
def profile_detail(request, user_id):
    user = User.objects.get(id=user_id)
    profile_form = Profile_Form()
    user_form = User_Form()
    context = {'user': user, 'profile_form': profile_form, 'login': AuthenticationForm(), 'signup': Register_Form()}
    return render(request, 'user/profile.html', context)
    
# --- Post Detail ---
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post_form = Post_Form(instance=post)
    context = {'post': post, 'login': AuthenticationForm(), 'signup': Register_Form(), 'post_form': post_form}
    return render(request, 'posts/detail.html', context)    
    
# --- Images ---

def showimage(request):
    
    lastimage= Image.objects.last()

    imagefile= lastimage.imagefile


    form= Image_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    
    context= {'imagefile': imagefile,
              'form': form
              }
    return render(request, 'user/images.html', context)

# --- Signup ---

def signup(request):
    error_message = ''
    if request.method == 'POST':
      form = Register_Form(request.POST)
      if form.is_valid():
        user = form.save()
        city_id = City.objects.get(id=request.POST['current_city'])
        profile = Profile.objects.create(user = user, current_city = city_id)
        profile.save()
        login(request, user)
        return redirect('profile_detail')
      else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# --- Login ---

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile_detail', user_id=user.id)
    else:
        return redirect('/accounts/login')

@login_required 
def profile_edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user_form = User_Form(request.POST, instance=user)
        profile_form = Profile_Form(request.POST, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_detail', user_id=user.id)
        else:
            user_form = User_Form(instance=user)
            profile_form = Profile_Form(instance=user.profile)
            context = {'user': user, 'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'user/edit.html', context)