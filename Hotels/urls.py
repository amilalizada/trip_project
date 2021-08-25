from django.urls import path
from Hotels.views import HotelsListView,HotelsSinglePage,ReservePage,ReviewSendView,SavedHotelView,SavedHotelListView,\
    AfterPaymentView,DeleteHotelFromWishlist
app_name = 'hotels_app'


urlpatterns = [
    path('hotels/',HotelsListView.as_view(),name='hotels'),
    path('hotels-single/<slug:slug>/',HotelsSinglePage.as_view(),name='hotels-single'),
    path('hotels-reserve/<int:pk>/',ReservePage.as_view(),name='hotels-reserve'),
    path('hotels-reviews/',ReviewSendView.as_view(),name='hotels-reviews'),
    path('save-hotel/<int:pk>/',SavedHotelView.as_view(),name='save_hotel'),
    path('saved-hotels/', SavedHotelListView.as_view(), name='saved_hotels'),
    path('after-payment/',AfterPaymentView.as_view(),name='after_payment'),
    path('delete-hotel/<int:pk>',DeleteHotelFromWishlist.as_view(),name='delete_hotel'),
]