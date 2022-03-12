from django.db import models

# Create your models here.

class usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    # id = models.AutoField(primary_key=True, **opciones) 
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contactmail = models.CharField(max_length=30)
    cellphone = models.PositiveIntegerField()

class menu(models.Model):
    nombre_platillo = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=1024)

class promociones(models.Model):
    nombre_promocion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1024)
    promocion_image = models.ImageField('view',blank=True,upload_to="media")

class booking(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    email = models.CharField(max_length=30)
    dia_hora_booking = models.DateTimeField()
    solicitud_especial = models.CharField(max_length=1024)
    number_people = models.PositiveBigIntegerField()

class restaurantes(models.Model):
    name_restaurant = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1024)
    restaurant_image = models.ImageField('view',blank=True,upload_to="media")