from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User

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
                return redirect('home')  
        else: 
                context = {'error':'Passwords do not match.'}
                return render(request, 'registration/signup.html', context)
    else:
            return render(request, 'registration/signup.html')
                    
