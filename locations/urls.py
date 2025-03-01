from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationView

router = DefaultRouter()
router.register(r'locations', LocationView)

urlpatterns = [
    path('api/', include(router.urls)),
]