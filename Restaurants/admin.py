from django.contrib import admin
from Restaurants.models import RestaurantImages, Restaurants,ToEatReason, OptionListTypeCheckbox,\
    OptionListTypeRadio, OptionsTypeCheckbox, OptionsTypeRadio, RestaurantMenuImages, ReviewRestaurant, SavedArticleRestaurants

admin.site.register(OptionListTypeCheckbox)
admin.site.register(OptionListTypeRadio)
admin.site.register(OptionsTypeCheckbox)
admin.site.register(OptionsTypeRadio)
admin.site.register(RestaurantImages)
admin.site.register(RestaurantMenuImages)
# admin.site.register(Restaurants)
admin.site.register(ToEatReason)
admin.site.register(ReviewRestaurant)
admin.site.register(SavedArticleRestaurants)

class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImages
    extra = 3
    
class RestaurantMenuImageInline(admin.TabularInline):
    model = RestaurantMenuImages
    extra = 3

@admin.register(Restaurants)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [ RestaurantImageInline,RestaurantMenuImageInline ]



# @admin.register(Restaurants)
# class RestaurantMenuAdmin(admin.ModelAdmin):
#     inlines = [ , ]

# Register your models here.
