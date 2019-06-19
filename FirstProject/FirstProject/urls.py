from django.contrib import admin
from django.urls import path
from . import LoginPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginPage.views),
]
