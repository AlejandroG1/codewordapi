# Create your views here.
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import restaurants, users, menu, promotions, booking
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import menuSerializer,CustomUserSerializer, restaurantsSerializer, usersSerializer, promotionsSerializer, bookingSerializer, CustomTokenObtainSerializer

class usersViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = users.objects.all()
        serializer_class = usersSerializer
    
class restaurantsViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = restaurants.objects.all()
        serializer_class = restaurantsSerializer

class menuViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = menu.objects.all()
        serializer_class = menuSerializer

class promotionsViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = promotions.objects.all()
        serializer_class = promotionsSerializer

class bookingViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = booking.objects.all()
        serializer_class = bookingSerializer
        import envioCorreo
        envioCorreo.__init__(data=booking.objects.all())


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
                                        'refresh_token': login_serializer.validated_data.get('refresh'),
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