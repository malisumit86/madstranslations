from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home,name = 'home'),
    path("upload", views.home,name = 'upload'),
    path("about", views.about,name = 'about'),
    path("contact", views.contact,name = 'contact'),
    path("textupload", views.textupload,name = 'textupload')
]
 