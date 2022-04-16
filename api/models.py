
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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255, unique=True)
    cellphone = models.IntegerField()
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


class menus(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_platillo = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=1024)
    restaurante_id = models.ForeignKey("restaurants", on_delete=models.CASCADE)

class promotions(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_promocion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1024)
    promocion_image = models.ImageField('view',blank=True,upload_to="media")
    restaurante_id = models.ForeignKey("restaurants", on_delete=models.CASCADE)
    
class bookings(models.Model):
    id = models.AutoField(primary_key=True)
    restaurante_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    email = models.CharField(max_length=30)
    dia_hora_booking = models.DateTimeField()
    solicitud_especial = models.CharField(max_length=1024)
    number_people = models.PositiveIntegerField()
    restaurante_id = models.ForeignKey("restaurants", on_delete=models.CASCADE)

class restaurants(models.Model):
    id = models.AutoField(primary_key=True)
    name_restaurant = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1024)
    restaurant_image = models.ImageField('view',blank=True,upload_to="media")
    

class type_users(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey("users", on_delete=models.CASCADE)
    type_users = models.CharField(max_length=50)