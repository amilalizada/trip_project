from rest_framework import serializers
from Restaurants.models import Restaurants , OptionListTypeCheckbox , OptionsTypeCheckbox , OptionListTypeRadio , OptionsTypeRadio ,\
     RestaurantImages,RestaurantMenuImages, ToEatReason, ReviewRestaurant
from Main.models import City
from Account.models import User
from dataclasses import dataclass, Field

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'name',
        )

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'surname',
        )

class OptionListTypeCheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionListTypeCheckbox
        fields = (
            'option_name',
        )

class OptionTypeCheckbox(serializers.ModelSerializer):
    option_inputs = OptionListTypeCheckboxSerializer(many=True)
    class Meta:
        model = OptionListTypeCheckbox
        fields = (
            'option_name',
            'option_svg_file',
            'option_inputs',
        )   

class OptionListTypeRadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionListTypeRadio
        fields = (
            'option_name',
        )

class OptionsTypeRadioSerializer(serializers.ModelSerializer):
    option_inputs = OptionListTypeRadioSerializer(many=True)
    class Meta:
        model = OptionListTypeRadio
        fields = (
            'option_name',
            'option_svg_file',
            'option_inputs',
        )



class RestaurantSerializer(serializers.ModelSerializer):
    user = AuthorSerializer()
    city = CitySerializer()
    checkbox_options = OptionListTypeCheckboxSerializer(many=True)
    radio_options = OptionListTypeRadioSerializer()

    class Meta:
        model = Restaurants
        fields = (
            'user',
            'name',
            'city',
            'checkbox_options',
            'radio_options',
            'image',
            'phone_number',
            'video',
            'website',
            'location',
            'open_time',
            'close_time',
            'description',
            'min_price',
            'max_price',
            'special_diets',
            'meals',
            'cuisines',
            'features',
            'created_at',
            'updated_at',
            'slug',
            'food_rating',
            'service_rating',
            'value_rating',
            'atmosphere_rating',
            'overall_rating',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["url"] = instance.get_absolute_url()
        return data

class RestaurantImagesSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = RestaurantImages
        fields = (
            'restaurant',
            'images',
        )

class RestaurantMenuImagesSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = RestaurantMenuImages
        fields = (
            'restaurant',
            'images',
        )

class ToEatReasonSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = ToEatReason
        fields = (
            'restaurant',
            'reason',
            'reason_images',
            'reason_rating',
            'reason_short_description',
        )

class ReviewRestaurantSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    user = AuthorSerializer()

    class Meta:
        model = ReviewRestaurant
        fields = (
            'user',
            'restaurant',
            'comment',
            'food_rating',
            'service_rating',
            'value_rating',
            'atmosphere_rating',
        )
