from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Image, Profile, City, Post
from .forms import Image_Form, City_Form, Post_Form, User_Form, Register_Form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# --- Base Views ---
def home(request):
    context = {'login': AuthenticationForm(), 'signup': Register_Form()}
    return render(request, 'home.html', context)

def about(request):
    context = {'login': AuthenticationForm(), 'signup': Register_Form()}
    return render(request, 'about.html', context)

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
            return redirect('user_index')
    users = Profile.objects.filter(user=request.user)
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
      form = Register_Form(request.POST)
      if form.is_valid():
        user = form.save()
        city_id = City.objects.get(id=request.POST['current_city'])
        profile = Profile.objects.create(user = user, current_city = city_id)
        profile.save()
        login(request, user)
        return redirect('user_index')
      else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# --- Login View ---

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile_detail', user_id=user.id)
    else:
        return redirect('/accounts/login')