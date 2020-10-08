from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Image
from .forms import ImageForm


# Create your views here.

# --- Base Views ---
def home(request):
    return render(request, 'home.html')
<<<<<<< HEAD

def about(request):
    return render(request, 'about.html')


# --- Image Views ---
=======
>>>>>>> submaster

def showimage(request):
    lastimage= Image.objects.last()
    imagefile= lastimage.imagefile

    form= ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    
    context= {'imagefile': imagefile,
              'form': form
              }
    #set the path for user images      
    return render(request, 'User/images.html', context)
