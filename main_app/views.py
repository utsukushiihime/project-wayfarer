from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

# --- Base Views ---
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


# def about(request):
#     return render(request, 'about.html')