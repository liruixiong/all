from django.shortcuts import render
from django.http import HttpResponse
from lrx import models

# Create your views here.

def index(request):
    type_list = models .Product.objects.values('type').distinct()
    name_list = models .Product.objects.values('name', 'type')
    title = "荣耀"
    return render(request=request, template_name='index.html', context=locals())
