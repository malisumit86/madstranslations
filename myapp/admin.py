from django.contrib import admin
from .models import Image
from myapp.models import Contact

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']


admin.site.register(Contact)

