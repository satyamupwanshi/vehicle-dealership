from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView


# Create your models here.

class Vehicle(models.Model):
    VEHICLE_TYPE = (
        ('Car', 'Car'),
        ('Bike', 'Bike'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    type = models.CharField(max_length=10, choices=VEHICLE_TYPE)
    is_sold = models.BooleanField(default=False)
    posted_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)  # <-- Add here


class VehicleCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    test_drive = models.BooleanField(default=False)
    date = models.DateField()
