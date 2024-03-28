from .models import Car, Brand, Category, Transmission
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(read_only=True)
    class Meta :
        model = Brand
        fields = ['id', 'brand', 'created_at', 'updated_at']
class CategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'category', 'created_at']

class TransmissionSerializer(serializers.ModelSerializer):
    transmission = serializers.CharField(read_only=True)
    class Meta:
        model = Transmission
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.category', read_only=True)
    brand = serializers.CharField(source='brand.brand', read_only=True)
    transmission = serializers.CharField(source='transmission.transmission', read_only=True)

    class Meta:
        model = Car
        fields = [
            'legal_number',
            'image_vehicle_number',
            'police_number',
            'release_year',
            'color',
            'series',
            'total_distance',
            'price',
            'car_type',
            'car_image',
            'created_at',
            'updated_at',
            'brand',
            'category',
            'transmission',
        ]
