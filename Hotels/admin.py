from django.contrib import admin
from Hotels.models import Hotel,HotelAmenities,HotelImages,RoomType,RoomTypeBeds,Reservation, \
ReviewRating,Reviews,PoliciesSubFeatures,Policies,ReviewFields,ChildCount,RoomAmenities,SavedArticle
# Register your models here.
admin.site.register(Hotel)
admin.site.register(HotelAmenities)
admin.site.register(HotelImages)
admin.site.register(Reservation)
admin.site.register(ReviewRating)
admin.site.register(ReviewFields)
admin.site.register(RoomTypeBeds)
admin.site.register(RoomType)
admin.site.register(Reviews)
admin.site.register(PoliciesSubFeatures)
admin.site.register(Policies)
admin.site.register(ChildCount)
admin.site.register(RoomAmenities)
admin.site.register(SavedArticle)