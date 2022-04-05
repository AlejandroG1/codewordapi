from rest_framework import serializers
from api.models import users
from api.models import restaurants
from api.models import menus
from api.models import promotions
from api.models import bookings
from api.models import type_users

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainSerializer(TokenObtainPairSerializer): 
    pass

class CustomusersSerializer(serializers.ModelSerializer):
    class Meta:
        model =users
        fields = ['username', 'email', 'name']

class usersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = ['id','permission', 'status', 'name', 'last_name', 'email', 'cellphone', 'username']

class menusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = menus
        fields = ['id','nombre_platillo', 'ingredientes', 'restaurante_id']

class promotionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = promotions
        fields = ['id','nombre_promocion', 'descripcion','promocion_image', 'restaurante_id']

class bookingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bookings
        fields = ['id','nombre_usuario', 'apellido_usuario', 'telefono', 'email', 'dia_hora_booking', 'solicitud_especial', 'number_people','restaurante_id']

class restaurantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurants
        fields = ['id','name_restaurant', 'descripcion','restaurant_image']

class type_usersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = type_users
        fields = ['id','id_user', 'type_users']





