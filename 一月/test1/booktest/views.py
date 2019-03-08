from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from booktest.models import ImageModel


# Create your views here.
# 展示上传图片的那个页面 以及提交图片的逻辑
def upload_image(request):
    if request.method == "GET":
        return render(request, 'index.html', locals())
    else:
        # 标题
        title = request.POST.get('title')
        f1 = request.FILES.get('img')  # 图片
        # 我们写一个路径
        fname = '%s%s' % (settings.MEDIA_ROOT, f1.name)
        print(fname)
        # 文件操作
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
            img = ImageModel()
            img.title = title
            img.image_url = '/static/media/{}'.format(f1.name)
            img.save()

        return HttpResponse('OK')


def show(request):
    imgs = ImageModel.objects.all()
    return render(request, 'show.html', locals())
