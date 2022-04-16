from dataclasses import field, fields
from rest_framework import serializers
from api.models import users
from api.models import restaurants
from api.models import menus
from api.models import promotions
from api.models import bookings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class permSerial(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class CustomTokenObtainSerializer(TokenObtainPairSerializer): 
    pass

class CustomusersSerializer(serializers.ModelSerializer):
    class Meta:
        model =users
        fields = ['username', 'email', 'name']

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'
        

    def create(self, validated_data):
            first_Content_Type = ContentType.objects.get_for_model(restaurants)
            second_Content_Type = ContentType.objects.get_for_model(bookings)
            third_Content_Type = ContentType.objects.get_for_model(promotions)
            fourth_Content_Type = ContentType.objects.get_for_model(menus)    

            first_default_permission = Permission.objects.get( codename = 'view_restaurants',content_type = first_Content_Type)
            second_default_permission = Permission.objects.get(codename = 'view_bookings', content_type = second_Content_Type)
            third_default_permission = Permission.objects.get(codename = 'view_promotions', content_type = third_Content_Type)
            fourth_default_permisssion = Permission.objects.get(codename = 'view_menus', content_type = fourth_Content_Type)
            fifth_default_permission = Permission.objects.get(codename = 'add_bookings', content_type = second_Content_Type)
            sixth_default_permission = Permission.objects.get(codename = 'change_bookings', content_type = second_Content_Type)



            user = users(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            user.user_permissions.add( first_default_permission,second_default_permission,
            third_default_permission,fourth_default_permisssion, fifth_default_permission, sixth_default_permission)
            return user
class menusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = menus
        fields = ['id','nombre_platillo', 'ingredientes','status', 'restaurante_id']


class promotionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = promotions
        fields = ['id','nombre_promocion', 'descripcion','promocion_image', 'status','restaurante_id']


class bookingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bookings

        fields = ['id','nombre_usuario', 'apellido_usuario', 'telefono', 'email', 'dia_hora_booking', 'solicitud_especial', 'number_people','status','restaurante_id']


class restaurantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurants
        fields = ['id','name_restaurant', 'descripcion','status','restaurant_image']






