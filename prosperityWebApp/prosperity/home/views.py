from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home/index.html')

def otp(request):
    return render(request, 'home/otp.html')

def yourself(request):
    return render(request, 'home/yourself.html')

def profileDetails(request):
    return render(request, 'profiles/profileDetails.html')

def profileDocuments(request):
    return render(request, 'profiles/profileDocuments.html')

def profileCoverage(request):
    return render(request, 'profiles/profileCoverage.html')

def profileNotification(request):
    return render(request, 'profiles/profileNotification.html')

def profilePayments(request):
    return render(request, 'profiles/profilePayments.html')

def profilePaymentsAddCards(request):
    return render(request, 'profiles/profilePaymentsAddCards.html')

def profilePaymentsAddBanks(request):
    return render(request, 'profiles/profilePaymentsAddBanks.html')

def profileFeedback(request):
    return render(request, 'profiles/profileFeedback.html')

def profileAbout(request):
    return render(request, 'profiles/profileAbout.html')

def bioage(request):
    return render(request, 'vitals/health/bioage.html')

# Create your views here.

