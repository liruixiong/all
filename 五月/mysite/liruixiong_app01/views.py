from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
# return HttpResponse("hello baby")

def baby(request):
    return render(request, 'lrx.html')
