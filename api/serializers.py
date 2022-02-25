from rest_framework import serializers
from api.models import usuarios
from api.models import restaurantes
from api.models import menu
from api.models import promociones
from api.models import booking

class usuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuarios
        fields = ['name', 'last_name', 'contactmail', 'cellphone']

class menuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = menu
        fields = ['nombre_platillo', 'ingredientes']

class promocionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = promociones
        fields = ['nombre_promocion', 'descripcion','promocion_image']

class bookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = booking
        fields = ['nombre_usuario', 'apellido_usuario', 'telefono', 'email', 'dia_hora_booking', 'solicitud_especial']

class restaurantesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurantes
        fields = ['name_restaurant', 'descripcion','restaurant_image']
