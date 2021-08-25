from django.urls import path
from Main.api.views import SubscriberCreateAPIView , MainSearchAPIView

app_name = 'api_main'

urlpatterns = [
    path('subscribe/',SubscriberCreateAPIView.as_view(),name='subscribe'),
    path('cities/',MainSearchAPIView.as_view(),name='cities')

]