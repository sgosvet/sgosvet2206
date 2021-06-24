from django.db import models
from datetime import datetime


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    email = models.EmailField(max_length=150, verbose_name='Email')
    tel = models.CharField(max_length=150, verbose_name='Telefono', unique=True)
    Localidad = models.CharField(max_length=150, verbose_name='Localidad', unique=True)
    fecha = models.DateTimeField(("Fecha"), auto_now=False, auto_now_add=False)
    mensaje = models.TextField()
    

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'ContactUs'
        ordering = ['id']