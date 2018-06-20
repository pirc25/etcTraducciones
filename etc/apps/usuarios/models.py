from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.



"""

SI ESTAS LEYENDO ESTO YA VUELVO

"""


class User(AbstractUser):
    is_traductor = models.BooleanField(default=False)
    def __str__(self):
    	return '{} {}'.format(self.first_name,self.last_name)


class Idioma(models.Model):
	nombre=models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)
"""
class Cliente(models.Model):
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	telefono = models.CharField(max_length=20)

	def __str__(self):
		return '{} {}'.format(self.nombre,self.apellido)
"""

class Cotizacion(models.Model):
	titulo=models.CharField(max_length=50)
	nombres=models.CharField(max_length=60)
	email = models.CharField(max_length=50)
	telefono = models.CharField(max_length=20)
	fecha_limite=models.DateField()
	file=models.FileField(upload_to="files",null=True, blank=True,default='vacio.zip')
	idioma_origen = models.ForeignKey(Idioma,null=False,blank=False,on_delete=models.CASCADE,related_name="idioma_origen")
	idioma_destino = models.ForeignKey(Idioma,null=False,blank=False,on_delete=models.CASCADE,related_name="idioma_destino")
	comentario=models.CharField(max_length=300,null=True,blank=True,default='NO HAY COMENTARIO')

	def __str__(self):
		return '{}'.format(self.titulo)

