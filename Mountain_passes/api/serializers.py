from .models import *
from rest_framework import serializers


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = ['id', 'name', 'fam', 'otc', 'email', 'phone']


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['id', 'latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'winter_level', 'spring_level', 'summer_level', 'autumn_level']

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class PassSerializer(serializers.ModelSerializer):
    tourist = TouristSerializer(read_only=True)
    coordinates = CoordinatesSerializer(read_only=True)
    levels = LevelSerializer(read_only=True)
    images = ImagesSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Pass
        fields = '__all__'
