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
    path("investment",views.investment, name = 'investment'),
    path("assets",views.assets, name = 'assets'),
    path("expense",views.expense, name = 'expense'),
    path("liabilities",views.liabilities, name = 'liabilities'),
    path("insurance",views.insurance, name = 'insurance'),
    path("savings",views.savings, name = 'savings'),

    path("one",views.one, name = 'one'),
    path("two",views.two, name = 'two'),
    path("three",views.three, name = 'three'),
    path("four",views.four, name = 'four'),

    path("mes_bmi",views.mes_bmi, name = 'mes_bmi'),
    path("mes_heartRate",views.mes_heartRate, name = 'mes_heartRate'),
    path("mes_sleep",views.mes_sleep, name = 'mes_sleep'),
    path("mes_waterIntake",views.mes_waterIntake, name = 'mes_waterIntake'),
    path("mes_calories",views.mes_calories, name = 'mes_calories'),
    path("mes_bp",views.mes_bp, name = 'mes_bp'),
    path("mes_bs",views.mes_bs, name = 'mes_bs'),
    path("mes_immunity",views.mes_immunity, name = 'mes_immunity'),
    path("mes_mentalHealth",views.mes_mentalHealth, name = 'mes_mentalHealth'),
    path("mes_eyeVision",views.mes_eyeVision, name = 'mes_eyeVision'),
    path("mes_eyeTest1",views.mes_eyeTest1, name = 'mes_eyeTest1'),
    path("mes_eyeTest2",views.mes_eyeTest2, name = 'mes_eyeTest2'),
    path("mes_eyeTest3",views.mes_eyeTest3, name = 'mes_eyeTest3'),
    path("mes_medication",views.mes_medication, name = 'mes_medication'),

    path("mes_income",views.mes_income, name = 'mes_income'),
    path("mes_expense",views.mes_expense, name = 'mes_expense'),
    path("mes_saving",views.mes_saving, name = 'mes_saving'),
    path("mes_RE",views.mes_RE, name = 'mes_RE'),
    path("mes_V",views.mes_V, name = 'mes_V'),
    path("mes_B",views.mes_B, name = 'mes_B'),
    path("mes_S",views.mes_S, name = 'mes_S'),
    
]