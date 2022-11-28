from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.site.site_header = "Prosperity Admin"
admin.site.site_title = "Prosperity Portal"
admin.site.index_title = "Welcome to Prosperity Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('home.urls')),
    path("otp",include('home.urls')),
    path("otp/yourself",include('home.urls')),
    path("genderDob",include('home.urls')),
    path("heightWeight",include('home.urls')),

    path("profileDetails",include('home.urls')),
    path("profileDocuments",include('home.urls')),
    path("profileCoverage",include('home.urls')),
    path("profileNotification",include('home.urls')),
    path("profilePayments",include('home.urls')),
    path("profilePaymentsAddCards",include('home.urls')),
    path("profilePaymentsAddBanks",include('home.urls')),
    path("profileFeedback",include('home.urls')),
    path("profileAbout",include('home.urls')),
    
    path("bioage",include('home.urls')), 
    path("sleep",include('home.urls')), 
    path("heartRate",include('home.urls')),   
    path("water",include('home.urls')),   
    path("steps",include('home.urls')),   
    path("bloodSugar",include('home.urls')), 
    path("bloodPressure",include('home.urls')),
    path("bmi",include('home.urls')),

    path("netWorth",include('home.urls')),
    path("income",include('home.urls')),
    path("investment",include('home.urls')),
    path("assets",include('home.urls')),
    path("expense",include('home.urls')),
    path("liabilities",include('home.urls')),
    path("insurance",include('home.urls')),
    path("savings",include('home.urls')),
    
    path("one",include('home.urls')),
    path("two",include('home.urls')),
    path("three",include('home.urls')), 
    path("four",include('home.urls')), 

    path("mes_bmi",include('home.urls')), 
    path("mes_heartRate",include('home.urls')), 
    path("mes_sleep",include('home.urls')), 
    path("mes_waterIntake",include('home.urls')), 
    path("mes_calories",include('home.urls')), 
    path("mes_bp",include('home.urls')),
    path("mes_bs",include('home.urls')),
    path("mes_immunity",include('home.urls')),
    path("mes_mentalHealth",include('home.urls')),
    path("mes_eyeVision",include('home.urls')),
    path("mes_eyeTest1",include('home.urls')),
    path("mes_eyeTest2",include('home.urls')),
    path("mes_eyeTest3",include('home.urls')),
    path("mes_medication",include('home.urls')),

    path("mes_income",include('home.urls')),
    path("mes_expense",include('home.urls')),
    path("mes_saving",include('home.urls')),
    path("mes_RE",include('home.urls')),
    path("mes_V",include('home.urls')),
    path("mes_B",include('home.urls')),
    path("mes_S",include('home.urls')),
    path("mes_assets",include('home.urls')),
    path("mes_inv",include('home.urls')),
    path("mes_FD",include('home.urls')),
    path("mes_Mf",include('home.urls')),
    path("mes_PPF",include('home.urls')),
    path("mes_digitalGold",include('home.urls')),
    path("mes_insurance",include('home.urls')),

]


urlpatterns += staticfiles_urlpatterns()
