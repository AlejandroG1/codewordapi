from rest_framework import serializers
from api.models import User
from api.models import restaurantes
from api.models import menu
from api.models import promociones
from api.models import booking
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainSerializer(TokenObtainPairSerializer): 
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['username', 'email', 'name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','permission', 'status', 'name', 'last_name', 'email', 'cellphone', 'username']

class menuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = menu
        fields = ['nombre_platillo', 'ingredientes', 'restaurante_id']

class promocionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = promociones
        fields = ['nombre_promocion', 'descripcion','promocion_image', 'restaurante_id']

class bookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = booking
        fields = ['nombre_usuario', 'apellido_usuario', 'telefono', 'email', 'dia_hora_booking', 'solicitud_especial', 'number_people','restaurante_id']

class restaurantesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurantes
        fields = ['name_restaurant', 'descripcion','restaurant_image']





