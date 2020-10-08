from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

# --- Base Views ---
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')