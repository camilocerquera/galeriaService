from django.db import models

#Tabla de imagenes
class Urls(models.Model):
 url=models.CharField(max_length=2048)
 date=models.DateTimeField()
 user=models.CharField(max_length=16)
 title =models.CharField(max_length=250)
 description =models.CharField(max_length=2048)

#Tabla de registro de contacto
class Contact(models.Model):
 name=models.CharField(max_length=300)
 email=models.EmailField(max_length=100)
 msg=models.CharField(max_length=2048)
 date =models.DateTimeField(blank=True, null=True)
