from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from api import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.usuariosViewSet)
router.register(r'restaurantes', views.restaurantesViewSet)
router.register(r'menu', views.menuViewSet)
router.register(r'promociones', views.promocionesViewSet)
router.register(r'booking', views.bookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]

handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'