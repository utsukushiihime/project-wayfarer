from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Image, User_Profile, City, Post
from .forms import Image_Form
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# --- Base Views ---
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def user(request):
    return render(request, 'user/profile.html')

def profile(request):
    return render(request, 'user/profile.html')

def index(request):
    return render(request, 'cities/index.html')

def api(request):
    return JsonResponse({"status": 200})

        
# View Profile
@login_required
def user_index(request):
    if request.method == 'POST':
        user_form = User_Form(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.user = request.user
            # save() to the db
            new_user.save()
            return redirect('cats_index')
    users = User_Profile.objects.filter(user=request.user)
    user_form = User_Form()
    context = {'user': user, 'user_form': user_form}
    return render(request, 'user/profile.html', context)
# --- Image Views ---

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


# --- Signup View ---

def signup(request):
    error_message = ''
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('user_index')
      else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)