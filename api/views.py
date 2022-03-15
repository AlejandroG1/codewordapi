# Create your views here.
from rest_framework import viewsets
from api.models import restaurantes, usuarios, menu, promociones, booking
from rest_framework.permissions import IsAuthenticated
from .serializers import menuSerializer, restaurantesSerializer, usuariosSerializer, promocionesSerializer, bookingSerializer

class usuariosViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = usuarios.objects.all()
        serializer_class = usuariosSerializer
    
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