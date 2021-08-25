from django.urls import path
from Hotels.api.views import HotelListView,GetUserView

app_name = 'api_hotel'

urlpatterns = [
    path('',HotelListView.as_view(),name='hotel'),
    path('user-profile/',GetUserView.as_view(),name='user_profile'),
]