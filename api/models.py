from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#Modelo de autentificacion 
class UsuarioManager(BaseUserManager):
    def _create_user(self ,name ,last_name ,email ,username ,cellphone ,password ,is_staff ,is_superuser ,permission ,status ,**extra_fields):
        user = self.model(
            name = name,
            last_name = last_name,
            email = email,
            username = username,
            cellphone = cellphone,
            is_staff = is_staff,
            is_superuser = is_superuser,
            permission = permission,
            status = status,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self, name, last_name, email , username, cellphone ,password = None , **extra_fields):
        return self._create_user(name, last_name, email ,username,cellphone ,password , True, False, 1, 1,  **extra_fields)


    def create_superuser(self, name, last_name, email, username, cellphone, password = None ,**extra_fields):
        return self._create_user(name, last_name, email ,username,cellphone ,password , True, True , 2, 2,  **extra_fields)


class users(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255, unique=True)
    cellphone = models.BigIntegerField()
    username = models.CharField(max_length=15, unique=True, blank=False, null=False)
    permission = models.IntegerField(default = 1)
    status = models.IntegerField(default = 1)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name', 'cellphone']

    def __str__(self):
        return "Usuario: '{0}' de nombre completo: '{1} {2}'".format(self.username,self.name,self.last_name)



#Modelos accesibles despues de logeo



class menu(models.Model):
    nombre_platillo = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=1024)
    restaurante_id = models.ForeignKey("restaurants", on_delete=models.CASCADE)

class promotions(models.Model):
    nombre_promocion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1024)
    promocion_image = models.ImageField('view',blank=True,upload_to="media")
    restaurante_id = models.ForeignKey("restaurants", on_delete=models.CASCADE)

class booking(models.Model):
    restaurante_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=30)
    dia_hora_booking = models.DateTimeField()
    solicitud_especial = models.CharField(max_length=1024)
    number_people = models.PositiveIntegerField()
    restaurante_id = models.ForeignKey("restaurants", on_delete=models.CASCADE)

class restaurants(models.Model):
    name_restaurant = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1024)
    restaurant_image = models.ImageField('view',blank=True,upload_to="media")