from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationView , MapView 
app_name = 'locations'
router = DefaultRouter()
router.register(r'locations', LocationView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('map/',MapView.as_view(),name='map')
    #path('map/', map_view, name='map'),
]