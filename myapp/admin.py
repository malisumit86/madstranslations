from django.contrib import admin
from .models import Image,Pdf
from myapp.models import Contact
# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']

@admin.register(Pdf)
class PdfAdmin(admin.ModelAdmin):
    list_display_pdf = ['id','pdf','date']

admin.site.register(Contact)

