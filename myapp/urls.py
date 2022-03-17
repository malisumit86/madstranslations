from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home,name = 'home'),
    path("upload", views.home,name = 'upload'),
    path("pdfupload", views.pdfupload,name = 'pdfupload'),
    path("about", views.about,name = 'about'),
    path("contact", views.contact,name = 'contact'),
    path("capture", views.capture,name = 'capture'),
    path("captured_translate", views.captured_translate,name = 'captured_translate'),
    path("textupload", views.textupload,name = 'textupload')
    
]
 