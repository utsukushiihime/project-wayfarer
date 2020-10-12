from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import City, Post, Profile
from .forms import Post_Form, Profile_Form, User_Form, Register_Form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# --- Base Views ---
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def api(request):
    return JsonResponse({"status": 200})

def profile(request):
    return render(request, 'profile/detail.html')

# --- Posts Index ---
@login_required
def posts_index(request):
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            # save(commit=False) will just make a copy/instance of the model
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            # save() to the db
            new_post.save()
            return redirect('posts_index')
    post = Post.objects.filter(user=request.user)
    posts = Post.objects.all()
    post_form = Post_Form()
    context = {'post': post, 'post_form': post_form, 'posts': posts}
    return render(request, 'posts/index.html', context)

# --- Post Detail ---
@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

# --- City Index ---
# FIXME Adding data all to view for testing
def cities_index(request):
    profile = Profile.objects.all()
    cities = City.objects.all()
    post = Post.objects.all()
    context = {'cities': cities, 'post': post, 'profile': profile}
    return render(request, 'cities/index.html', context)

    # if request.method == 'POST':
    #     city_form = City_Form(request.POST)
    #     if city_form.is_valid():
    #         new_city = city_form.save(commit=False)
    #         new_city.user = request.user
    #         new_city.save()
    #         return redirect('cities_index')
    #     cities = City.objects.all()
    #     profile = Profile.objects.all()  
    #     post = Post.objects.all()
    #     city_form = City_Form()
    #     context = {'cities': cities, 'city_form': city_form, 'profile': profile, 'post': post, 'login': AuthenticationForm(), 'signup': UserCreationForm()}
        # return render(request,'cities/index.html', context)

# --- City Detail ---
def cities_detail(request, city_id):
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city_id=city.id)
    post = Post.objects.all()
    post_form = Post_Form()
    context = {'login': AuthenticationForm(), 'post': post, 'signup': UserCreationForm(), 'city': city, 'post_form': post_form, 'posts': posts}
    return render(request, 'cities/detail', context)
        
# --- Profile Detail ---
def profile_detail(request, user_id):
    user = User.objects.get(id=user_id)
    profile_form = Profile_Form()
    user_form = User_Form()
    context = {'user': user, 'profile_form': profile_form, 'login': AuthenticationForm(), 'signup': UserCreationForm(), 'user_form': user_form}
    return render(request, 'profile/detail.html', context)

# --- Signup ---
# FIXME create user profile on signup
# def signup(request):
#     if request.method == 'POST':
#         form = Register_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      return redirect('login')
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
        return redirect('home', user_id=user.id)
    else:
        return redirect('home')

@login_required 
def profile_edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        # user_form = User_Form(request.POST, instance=user)
        profile_form = Profile_Form(request.POST, instance=user.profile)
        if profile_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            # user_form.save()
            return redirect('profile_detail', user_id=user.id)
        else:
            user_form = User_Form(instance=user)
            profile_form = Profile_Form(instance=user.profile)
            context = {'user': user, 'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'profile/edit.html', context)