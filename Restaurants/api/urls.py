from django.urls import path
from Restaurants.api.views import restaurants_api \
    # restaurants_query 

app_name = 'api_restaurant'

urlpatterns = [
    path('',restaurants_api, name = 'restaurants_api'),
    # path('search/',restaurants_query,name = 'restaurants_query')
]