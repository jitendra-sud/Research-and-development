from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def otp(request):
    return render(request, 'otp.html')

def yourself(request):
    return render(request, 'yourself.html')

def profileDetails(request):
    return render(request, 'profileDetails.html')

def profileDocuments(request):
    return render(request, 'profileDocuments.html')

def profileCoverage(request):
    return render(request, 'profileCoverage.html')

def profileNotification(request):
    return render(request, 'profileNotification.html')



# Create your views here.
