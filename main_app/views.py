from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import Image
# from .forms import Image_Form


# Create your views here.

# --- Base Views ---
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'user/profile.html')

def index(request):
    return render(request, 'cities/index.html')


# index and create

def post_index(request):
    if request.method == 'POST':
        post_form = Cat_Form(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect()



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
    #set the path for user images      
    return render(request, 'User/images.html', context)
