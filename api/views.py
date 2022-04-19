# Create your views here.
from django import views
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import restaurants, users, menus, promotions, bookings, type_users
from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import menusSerializer,CustomusersSerializer, restaurantsSerializer, usersSerializer, promotionsSerializer, bookingsSerializer, CustomTokenObtainSerializer, type_usersSerializer, permSerial
class ActualDjangoModelPermissions(DjangoModelPermissions):
    view_permissions = ['%(app_label)s.view_%(model_name)s']
    perms_map = {
        'GET': view_permissions,
        'OPTIONS': view_permissions,
        'HEAD': view_permissions,
        'POST': DjangoModelPermissions.perms_map['POST'],
        'PUT': DjangoModelPermissions.perms_map['PUT'],
        'PATCH': DjangoModelPermissions.perms_map['PATCH'],
        'DELETE': DjangoModelPermissions.perms_map['DELETE'],
    }

class permissionViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated, ActualDjangoModelPermissions,]
        queryset = Permission.objects.all()
        serializer_class = permSerial

class usersViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated, ActualDjangoModelPermissions,]
        queryset = users.objects.all()
        serializer_class = CustomusersSerializer

class type_usersViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated, ActualDjangoModelPermissions,]
        queryset = type_users.objects.all()
        serializer_class = type_usersSerializer

class restaurantsViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated, ActualDjangoModelPermissions,]
        queryset = restaurants.objects.all()
        serializer_class = restaurantsSerializer

class menusViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated, ActualDjangoModelPermissions,]
        queryset = menus.objects.all()
        serializer_class = menusSerializer

class promotionsViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated, ActualDjangoModelPermissions,]
        queryset = promotions.objects.all()
        serializer_class = promotionsSerializer

class bookingsViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated, ActualDjangoModelPermissions,]
        queryset = bookings.objects.all()
        serializer_class = bookingsSerializer
        





#ACCESOS
class register(GenericAPIView):
        serializer_class = usersSerializer
        def post(self, request, *arg, **kwargs):
                user_serializer = self.serializer_class(data=request.data)
                if user_serializer.is_valid():
                        user_serializer.save()
                        return Response({'success':'registrado'}, status= status.HTTP_201_CREATED)
                return Response({'failed':'usuario no creado',
                                 'error': user_serializer.errors}, status= status.HTTP_400_BAD_REQUEST)

class login(TokenObtainPairView):
        serializer_class = CustomTokenObtainSerializer
        def post(self, request, *args, **kwargs):
                username = request.data.get('username', '')
                password = request.data.get('password', '')
                user = authenticate(username=username, password=password)
               
                if user:
                        login_serializer = self.serializer_class(data=request.data)
                        if login_serializer.is_valid():
                                user_serializer = CustomusersSerializer(user)
                                return Response({
                                        'token': login_serializer.validated_data.get('access'),
                                        'refresh-token': login_serializer.validated_data.get('refresh'),
                                        'user': user_serializer.data,
                                        'message': 'inicio de sesion correcto'
                                }, status = status.HTTP_200_OK)
                        return Response({'error': 'Contraseña o usuario incorrecto'}, status = status.HTTP_400_BAD_REQUEST )
                return Response({'error': 'Contraseña o usuario incorrecto'}, status = status.HTTP_400_BAD_REQUEST )

class logout(GenericAPIView):
        def post(self, request, *args, **kwargs):
                user = users.objects.filter(id=request.data.get('username', 0))
                print(user)
                if user.exists():
                        RefreshToken.for_user(user.first())
                        return Response({'message': 'Sesion terminada'}, status = status.HTTP_200_OK)
                return Response({'error': 'No existe el usuario'}, status = status.HTTP_400_BAD_REQUEST )

