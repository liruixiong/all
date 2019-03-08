from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    ctx = {'title': "荣耀"}
    return render(request=request, template_name='index.html')
