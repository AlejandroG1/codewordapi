# Create your views here.
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import restaurantes, User, menu, promociones, booking
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import menuSerializer,CustomUserSerializer, restaurantesSerializer, UserSerializer, promocionesSerializer, bookingSerializer, CustomTokenObtainSerializer

class usuariosViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = User.objects.all()
        serializer_class = UserSerializer
    
class restaurantesViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = restaurantes.objects.all()
        serializer_class = restaurantesSerializer

class menuViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = menu.objects.all()
        serializer_class = menuSerializer

class promocionesViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = promociones.objects.all()
        serializer_class = promocionesSerializer

class bookingViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = booking.objects.all()
        serializer_class = bookingSerializer


class login(TokenObtainPairView):
        serializer_class = CustomTokenObtainSerializer
        def post(self, request, *args, **kwargs):
                username = request.data.get('username', '')
                password = request.data.get('password', '')
                user = authenticate(username=username, password=password)
               
                if user:
                        login_serializer = self.serializer_class(data=request.data)
                        if login_serializer.is_valid():
                                user_serializer = CustomUserSerializer(user)
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
                user = User.objects.filter(id=request.data.get('username', 0))
                print(user)
                if user.exists():
                        RefreshToken.for_user(user.first())
                        return Response({'message': 'Sesion terminada'}, status = status.HTTP_200_OK)
                return Response({'error': 'No existe el usuario'}, status = status.HTTP_400_BAD_REQUEST )