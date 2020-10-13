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

# def profile(request):
#     return render(request, 'profile/detail.html')

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

@login_required 
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = Post_Form(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post_detail', post_id=post.id)
        else:
            post_form = Post_Form(instance=post)
            context = {'post': post, 'post_form': post_form}
            return render(request, 'posts/edit.html', context)

# --- Post delete ---

@login_required
def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect("posts_index")

# --- City Index ---
# FIXME Adding data all to view for testing
def cities_index(request):
    profile = Profile.objects.all()
    cities = City.objects.all()
    post = Post.objects.all()
    context = {'cities': cities, 'posts': post, 'profile': profile}
    return render(request, 'cities/index.html', context)

# --- City Detail ---
def cities_detail(request, city_id):
    cities = City.objects.all()
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city_id=city.id)
    post = Post.objects.all()
    post_form = Post_Form()
    context = {'login': AuthenticationForm(), 'post': post, 'signup': UserCreationForm(), 'city': city, 'cities': cities, 'post_form': post_form, 'posts': posts.order_by("-created_at")}
    return render(request, 'cities/detail.html', context)

        
# --- Profile Detail ---
# def profile_detail(request):
#     print(request.user.id)
#     user = User.objects.get(id=request.user.id)
#     profile_form = Profile_Form()
#     user_form = User_Form()
#     posts = Post.objects.filter(user = request.user.id)
#     context = {'user': user, 'profile_form': profile_form, 'login': AuthenticationForm(), 'signup': UserCreationForm(), 'user_form': user_form}
#     return render(request, 'profile/detail.html', context)

# def profile_detail(request, user_id):
#     user = Post.objects.filter(user_id = request.user.id)
#     post_form = Post_Form()
#     posts = Post.objects.filter(user = request.user.id)
#     context = {'user': user, 'user_id': user_id, 'posts': posts, 'post_form': post_form}
#     return render(request, 'profile/detail.html', context)

def profile_detail(request):
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(user = user)
    context = {'posts': posts}
    return render(request, 'profile/profile.html', context)


# --- Profile delete ---

@login_required
def profile_delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("home")


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = Register_Form(request.POST)
    profile_form = Profile_Form(request.POST)
    if form.is_valid() and profile_form.is_valid(): 
        user = form.save()
        print('form', form)
        new_profile = profile_form.save(commit=False)
        new_profile.user=user
        new_profile.save()
        login(request, user)
        return redirect('profile')#, user_id = user.id)
    else:
      error_message = 'Invalid sign up - try again'
  form = Register_Form()
  profile = Profile_Form()
  context = {'form': form, 'profile' : profile, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)




# --- Login ---

def login_user(request):
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
            return redirect('profile', user_id=user.id)
        else:
            user_form = User_Form(instance=user)
            profile_form = Profile_Form(instance=user.profile)
            context = {'user': user, 'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'profile/edit.html', context)