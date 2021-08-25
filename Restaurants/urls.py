from django.urls import path
from Restaurants.views import RestaurantsListView, RestaurantsSinglePageClassView , ReviewCreateView, SavedRestaurantView, SavedRestaurantListView,SavedRestaurantView

app_name = 'restaurants_app'

urlpatterns = [
    path('saved-restaurants/',SavedRestaurantListView.as_view(),name ='saved_wishlist'),
    path('',RestaurantsListView.as_view(),name='restaurants'),
    path('review/',ReviewCreateView.as_view(),name='restaurants_review'),
    path('<slug:slug>/',RestaurantsSinglePageClassView.as_view(),name='restaurant_single_page'),
    path('saved-restaurants/<int:pk>/',SavedRestaurantView.as_view(),name ='save_wishlist'),


]