from rest_framework import serializers
from Main.models import Subscriber,City
from Hotels.models import Hotel
from Tours.models import Tours
from Restaurants.models import Restaurants


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email',)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',
                  'main_image',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["url"] = instance.get_absolute_url()
        return data

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ('name',
                  )


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurants
        fields = ('name',
        'image',
                  )


class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tours
        fields = ('name',
                'main_image',
                  )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["url"] = instance.get_absolute_url()
        return data


