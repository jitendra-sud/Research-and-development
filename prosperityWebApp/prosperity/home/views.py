from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home/index.html')

def otp(request):
    return render(request, 'home/otp.html')

def yourself(request):
    return render(request, 'home/yourself.html')

def genderDob(request):
    return render(request,'home/genderDob.html')

def heightWeight(request):
    return render(request,'home/heightWeight.html')




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

def sleep(request):
    return render(request, 'vitals/health/sleep.html')

def heartRate(request):
    return render(request, 'vitals/health/heartRate.html')

def water(request):
    return render(request, 'vitals/health/water.html')

def steps(request):
    return render(request, 'vitals/health/steps.html')

def bloodSugar(request):
    return render(request, 'vitals/health/bloodSugar.html')

def bloodPressure(request):
    return render(request, 'vitals/health/bloodPressure.html')

def bmi(request):
    return render(request, 'vitals/health/bmi.html')




def netWorth(request):
    return render(request, 'vitals/wealth/netWorth.html')

def income(request):
    return render(request, 'vitals/wealth/income.html')

def investment(request):
    return render(request, 'vitals/wealth/investment.html')

def assets(request):
    return render(request, 'vitals/wealth/assets.html')

def expense(request):
    return render(request, 'vitals/wealth/expense.html')

def liabilities(request):
    return render(request, 'vitals/wealth/liabilities.html')

def insurance(request):
    return render(request, 'vitals/wealth/insurance.html')

def savings(request):
    return render(request, 'vitals/wealth/savings.html')



def one(request):
    return render(request, 'buyPolicy/one.html')

def two(request):
    return render(request, 'buyPolicy/two.html')

def three(request):
    return render(request, 'buyPolicy/three.html')

def four(request):
    return render(request, 'buyPolicy/four.html')



def mes_bmi(request):
    return render(request, 'measures/bmi.html')

# Create your views here.



