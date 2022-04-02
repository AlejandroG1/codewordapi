from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from api import views
from api.views import login, logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r'users', views.usersViewSet)
router.register(r'restaurants', views.restaurantsViewSet)
router.register(r'menus', views.menusViewSet)
router.register(r'promotions', views.promotionsViewSet)
router.register(r'bookings', views.bookingsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', login.as_view(), name= 'login'),
    path('logout/', logout.as_view(), name='logout'),
    #usar login path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]

handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'