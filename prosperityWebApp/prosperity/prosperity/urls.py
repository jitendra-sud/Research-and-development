from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Prosperity Admin"
admin.site.site_title = "Prosperity Portal"
admin.site.index_title = "Welcome to Prosperity Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('home.urls'))
]
