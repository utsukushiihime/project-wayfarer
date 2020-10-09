from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

# Create your views here.

#---Registration View ---
def register(request):
    if request.method == "POST":
        username_form = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username already exists.'}
                return render (request, 'registration/signup.html', context)
            
            else:
                user = User.objects.create_user(
                    username = username_form,
                    password = password)
                user.save()
                return redirect('registration/login.html')
        else: 
                context = {'error':'Passwords do not match.'}
                return render(request, 'registration/signup.html', context)
    else:
            return render(request, 'registration/signup.html')


#--- login view ---

#@login_required
def login(request):
  if request.method == 'POST':
    username_form = request.POST['username']
    password_form = request.POST['password']
    user = auth.authenticate(username=username_form, password=password_form)
    if user is not None:
      auth.login(request, user)
      return redirect('user/profile.html') 
    else:
      context = {'error':'Invalid Credentials'}
      return render(request, 'registration/login.html', context)
  else:
    return render(request, 'registration/login.html')

#-- logout view ---
def logout(request):
    auth.logout(request)
    return redirect('home')
                    
