from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name = 'home'),
    path("otp",views.otp,name = 'otp'),
    path("otp/yourself",views.yourself, name = 'yourself'),
    path("profileDetails",views.profileDetails, name = 'profileDetails'),
    path("profileDocuments",views.profileDocuments, name = 'profileDocuments'),
    path("profileCoverage",views.profileCoverage, name = 'profileCoverage'),
]