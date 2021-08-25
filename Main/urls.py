
from django.urls import path
from Main.views import MainClassView,SubscriberCreateView,ContactSubjectView,ContactPageView,AboutUsView,PrivacyPolicyView, \
    TermsOfUseView,CitySinglePage,CitiesPage


app_name = 'main'


urlpatterns = [

    path('',MainClassView.as_view(),name='home'),
    path('subscribe/',SubscriberCreateView.as_view(),name='subscribe'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('contact-form/',ContactSubjectView.as_view(),name='contact-form'),
    path('about-us/',AboutUsView.as_view(),name='about-us'),
    path('privacy/',PrivacyPolicyView.as_view(),name='privacy'),
    path('terms/',TermsOfUseView.as_view(),name='terms'),
    path('cities/<slug:slug>/',CitySinglePage.as_view(),name='city-detail'),
    path('cities/',CitiesPage.as_view(),name='cities_list')
]