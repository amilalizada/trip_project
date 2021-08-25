from django.urls import path
from Places.views import  PlacesClassView,PlacesSinglePageClassView

app_name = 'places_app'

urlpatterns = [
    path('',PlacesClassView.as_view(),name='places'),
    path('single-page/',PlacesSinglePageClassView.as_view(),name='place_single_page'),
]