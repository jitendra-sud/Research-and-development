from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def name(request):
    return HttpResponse('Fuck You!')

# Create your views here.
