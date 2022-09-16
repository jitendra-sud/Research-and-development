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
    path("profileDetails",include('home.urls')),
    path("profileDocuments",include('home.urls')),
    path("profileCoverage",include('home.urls')),
    path("profileNotification",include('home.urls')),
]

urlpatterns += staticfiles_urlpatterns()
