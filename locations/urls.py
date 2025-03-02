from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationView , MapView , search_nearby , add_location , export_locations 
app_name = 'locations'
router = DefaultRouter()
router.register(r'locations', LocationView)

urlpatterns = [
    path('api/', include(router.urls)),
   
    path('',MapView.as_view(),name='map'),
    path('search_nearby/', search_nearby, name='search_nearby'),
    path('add/', add_location, name='add_location'),
    path('export/<str:format>/', export_locations, name='export_locations'),
    #path('map/', map_view, name='map'),
]