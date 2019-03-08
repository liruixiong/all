from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    s = request.path
    return HttpResponse(s)


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        account = request.POST.get('account')
        pwd = request.POST.get('pwd')
        s = '账号是：{}  密码是：{}'.format(account, pwd)
        return HttpResponse(s)
