from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def main(requeste):
    return HttpResponse("<h1>salom</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main)
]
