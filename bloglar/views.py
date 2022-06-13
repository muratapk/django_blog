from django.shortcuts import render,HttpResponse

# Create your views here.
# def index(request):
#     text="Merhabalar"
#     return HttpResponse(text)
# def about(request):
#     text="Merhabalar"
#     return HttpResponse(text)
# herhangi sayfa olmadan ekrana veri yazırmak için 


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'template/about.html')
