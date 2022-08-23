from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def otp(request):
    return render(request, 'otp.html')

def yourself(request):
    return render(request, 'yourself.html')


# Create your views here.
