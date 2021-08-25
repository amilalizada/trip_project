from rest_framework.generics import CreateAPIView
from Main.api.serializers import SubscriberSerializer , CitySerializer , HotelSerializer , RestaurantSerializer , TourSerializer
from rest_framework.authentication import BasicAuthentication
from Main.api.utils import CsrfExemptSessionAuthentication
from rest_framework.views import APIView
from Main.models import City 
from Hotels.models import Hotel
from Tours.models import Tours
from Restaurants.models import Restaurants
from rest_framework.response import Response
from itertools import chain
import json



class SubscriberCreateAPIView(CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
    serializer_class = SubscriberSerializer


class MainSearchAPIView(APIView):
    # serializer_class = CitySerializer
    # def get_queryset(self):
    #     query_list = []
    #     print(self.request.GET.get('inputValue'))
    #     input_value = self.request.GET.get('inputValue')
    #     queryset = City.objects.filter(name__icontains=input_value)
     

    #     return queryset
    
    
     def get(self,request):
        input_value = self.request.GET.get('inputValue')
        print(input_value)
    
        city_query = City.objects.filter(name__icontains=input_value)[:2]
        hotel_query = Hotel.objects.filter(name__icontains=input_value)[:2]
        tour_query = Tours.objects.filter(name__icontains=input_value)[:2]
        restaurant_query = Restaurants.objects.filter(name__icontains=input_value)[:2]

    

        city_serializer = CitySerializer(city_query, many=True,context={'request':request})
        hotel_serializer = HotelSerializer(hotel_query, many=True)
        restaurant_serializer = RestaurantSerializer(restaurant_query, many=True,context={'request':request})
        tour_serializer = TourSerializer(tour_query, many=True,context={'request':request})

        # data = {
        #     "cities": city_serializer.data,
        #     "hotels": hotel_serializer.data,
        #     "restaurant": restaurant_serializer.data,
        #     "tour": tour_serializer.data,
        # }
        data_obj = list(chain(city_serializer.data,hotel_serializer.data,restaurant_serializer.data,tour_serializer.data,))
        # json_data = json.dumps(data_obj)
   
        data = {
            "data_obj":data_obj,
        }
        print(data)
        return Response(data)