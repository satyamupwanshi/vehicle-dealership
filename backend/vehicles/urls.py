from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, RegisterView  # ✅ import both in one line

# Set up router for Vehicle APIs
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)  # ✅ give a prefix here

# Define your URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Handles /api/vehicles/
    path('register/', RegisterView.as_view(), name='register'),  # Handles /api/register/
]
