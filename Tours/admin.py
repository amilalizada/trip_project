from django.contrib import admin
from Tours.models import *

# admin.site.register(Tours)
admin.site.register(TourComments)
admin.site.register(TourImages)
admin.site.register(Inclusion)
admin.site.register(Activites)
admin.site.register(ImportantNotes)
admin.site.register(RightRorYou)
admin.site.register(WhyYouLove)
admin.site.register(SavedArticleTour)

class TourImageInline(admin.TabularInline):
    model = TourImages
    extra = 3

@admin.register(Tours)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [ TourImageInline, ]

