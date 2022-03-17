from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to = 'myimage')
    date = models.DateTimeField(auto_now=True)

class Capture(models.Model):
    photo = models.ImageField(upload_to = 'Capture')
    date = models.DateTimeField(auto_now=True)

class Pdf(models.Model):
    pdf = models.FileField(upload_to = 'mypdf')
    date = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    mail = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    Address = models.CharField(max_length=122)
    Address2 = models.CharField(max_length=122)
    mob_num = models.IntegerField()
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mail
