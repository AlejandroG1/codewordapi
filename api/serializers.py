from rest_framework import serializers
from api.models import users
from api.models import restaurants
from api.models import menu
from api.models import promotions
from api.models import booking
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainSerializer(TokenObtainPairSerializer): 
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =users
        fields = ['username', 'email', 'name']

class usersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = ['id','permission', 'status', 'name', 'last_name', 'email', 'cellphone', 'username']

class menuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = menu
        fields = ['nombre_platillo', 'ingredientes', 'restaurante_id']

class promotionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = promotions
        fields = ['nombre_promocion', 'descripcion','promocion_image', 'restaurante_id']

class bookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = booking
        fields = ['nombre_usuario', 'apellido_usuario', 'telefono', 'email', 'dia_hora_booking', 'solicitud_especial', 'number_people','restaurante_id']

class restaurantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurants
        fields = ['name_restaurant', 'descripcion','restaurant_image']





