from django.shortcuts import render

# Create your views here.

def indexVista(request):
    return render(request, 'index.html')