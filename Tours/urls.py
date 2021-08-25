from django.urls import path
from Tours.views import *

app_name = 'tours'

urlpatterns = [
    path('',ToursPage.as_view(),name ='tours-list'),
    path('wishlist/', SavedTourListView.as_view(), name='saved_wishlist'),
    path('<slug:slug>/',ToursSinglePage.as_view(),name ='tour-detail'),  
    path('save-tour/<int:pk>/',SavedTourView.as_view(),name ='save_wishlist'),
    
]