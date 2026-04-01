from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about(request):
    # return render(request, 'core/about.html')
    return HttpResponse("This is the about page")
