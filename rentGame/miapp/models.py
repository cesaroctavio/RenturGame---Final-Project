# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.
class Usuario(models.Model):
     nombre=models.OneToOneField(User)
     telefono=models.IntegerField()
     email=models.CharField(max_length=30)
     address=models.CharField(max_length=30)

     def __unicode__(self):
         return self.nombre.username

class VideoJuego(models.Model):
    nombre = models.CharField(max_length = 50)
    imagen = models.ImageField(upload_to="imagenes")

    def __unicode__(self):
        return self.nombre
