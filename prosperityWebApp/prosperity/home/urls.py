from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name = 'home'),
    path("otp",views.otp,name = 'otp'),
    path("otp/yourself",views.yourself, name = 'yourself'),
    path("genderDob", views.genderDob, name = 'genderDob'),
    
    path("heightWeight", views.heightWeight, name = 'heightWeight'),
    path("profileDetails",views.profileDetails, name = 'profileDetails'),
    path("profileDocuments",views.profileDocuments, name = 'profileDocuments'),
    path("profileCoverage",views.profileCoverage, name = 'profileCoverage'),
    path("profileNotification",views.profileNotification, name = 'profileNotification'),
    path("profilePayments",views.profilePayments, name = 'profilePayments'),
    path("profilePaymentsAddCards",views.profilePaymentsAddCards, name = 'profilePaymentsAddCards'),
    path("profilePaymentsAddBanks",views.profilePaymentsAddBanks, name = 'profilePaymentsAddBanks'),
    path("profileFeedback",views.profileFeedback, name = 'profileFeedback'),
    path("profileAbout",views.profileAbout, name = 'profileAbout'),
    
    path("bioage",views.bioage, name = 'bioage'),
    path("sleep",views.sleep, name = 'sleep'),
    path("heartRate",views.heartRate, name = 'heartRate'),
    path("water",views.water, name = 'water'),
    path("steps",views.steps, name = 'steps'),
    path("bloodSugar",views.bloodSugar, name = 'bloodSugar'),
    path("bloodPressure",views.bloodPressure, name = 'bloodPressure'),
    path("bmi",views.bmi, name = 'bmi'),

    path("netWorth",views.netWorth, name = 'netWorth'),
    path("income",views.income, name = 'income'),
]