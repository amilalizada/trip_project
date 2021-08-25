from rest_framework import serializers
from Hotels.models import Hotel,RoomTypeBeds,HotelAmenities,RoomType,HotelImages,ReviewFields,\
    ReviewRating,Reservation,Reviews,Policies,PoliciesSubFeatures,SavedArticle
from Account.models import User
from Main.api.serializers import CitySerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',
                  'image',
                  'name',
                  'surname',)

class RoomTypeBedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTypeBeds
        fields = ('count',)

class ReviewFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewFields
        fields = ('title',)

class ReviewRatingSerializer(serializers.ModelSerializer):
    review_field = ReviewFieldSerializer(many=True)
    class Meta:
        model = ReviewRating
        fields = ('rating_point',
                  'review_field',)

class HotelAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAmenities
        fields = ('name',
                  'image',
                  'sub_or_main',)

class RoomTypeSerializer(serializers.ModelSerializer):
    beds = RoomTypeBedsSerializer(many=True )
    class Meta:
        model = RoomType
        fields = ('title',
                  'description',
                  'price',
                  'beds',)
class PoliciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policies
        fields = ('title',)

class PoliciesSubSerializer(serializers.ModelSerializer):
    policies = PoliciesSerializer()
    class Meta:
        model = PoliciesSubFeatures
        fields = ('title',
                  'policies',)



class HotelSerializer(serializers.ModelSerializer):
    city=CitySerializer()
    author= UserSerializer()
    policies=PoliciesSerializer(many=True)
    room_type=RoomTypeSerializer(many=True)
    review_fields=ReviewFieldSerializer(many=True)
    class Meta:
        model = Hotel
        fields = ('id',
                  'name',
                  'name_description',
                  'short_description',
                  'long_description',
                  'longitude',
                  'latitude',
                  'phone_number',
                  'website',
                  'rating',
                  'main_image',
                  'city',
                  'author',
                  'policies',
                  'room_type',
                  'review_fields',
                  'slug',
                  'min_price',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["my_url"] = instance.get_absolute_url()
        return data

class HotelImageSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    class Meta:
        model = HotelImages
        fields = ('image',
                  'is_main',
                  'hotel',)





class ReservationSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()
    user= UserSerializer()
    hotel = HotelSerializer()
    class Meta:
        model = Reservation
        fields = (
                  'reservation_start_date',
                  'reservation_fin_date',
                  'price',
                  'note',
                  'day_count',
                  'room_type',
                  'user',
                  'hotel',)

class ReviewSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer()
    review_rating= ReviewRatingSerializer(many=True)
    class Meta:
        model = Reviews
        fields = ('title',
                  'subject',
                  'reservation',
                  'review_rating',
                  'created_at',)

class SavedArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    hotel= HotelSerializer()
    class Meta:
        model = SavedArticle
        fields = ('user',
                  'hotel',
                  'created_at',
                  'updated_at',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["my_url"] = instance.get_absolute_url()
        return data