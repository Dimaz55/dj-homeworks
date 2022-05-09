from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from advertisements.views import AdvertisementViewSet, FavAdvertisementViewSet

router = DefaultRouter()
router.register('advertisements', AdvertisementViewSet)
router.register('favs', FavAdvertisementViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
] + router.urls
