from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from Hotels.api.serializers import HotelSerializer,UserSerializer,ReservationSerializer,SavedArticleSerializer
from Hotels.models import Hotel,Reservation,SavedArticle
from Account.models import User
import math
from rest_framework.response import Response
import requests
import json




class HotelListView(APIView):

    def get(self,request):
        data = request.GET
        hotelAmenities=data.getlist('hotel_amenities[]')
        roomAmenities = data.getlist('room_amenities[]')
        cityName=data.get('cityName')
        selectedBed = data.get('selectedBed')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        selectedChildCount = data.get('selectedChildCount')
        filtered_hotels = Hotel.objects.all()
        if cityName :
            filtered_hotels=filtered_hotels.filter(city__name__icontains=cityName).distinct()
        if selectedBed:
            filtered_hotels = filtered_hotels.filter(room_type__beds__count=selectedBed).distinct()
        if selectedChildCount:
            filtered_hotels = filtered_hotels.filter(room_type__child_count__count=selectedChildCount).distinct()
        if minPrice:
            filtered_hotels=filtered_hotels.filter(min_price__gte=minPrice).distinct()
        if maxPrice:
            filtered_hotels=filtered_hotels.filter(min_price__lte=maxPrice).distinct()
        if hotelAmenities:
            for hotelAmenity in hotelAmenities:
                filtered_hotels = filtered_hotels.filter(hotel_amenity__name=hotelAmenity)
        if roomAmenities:
            for roomAmenity in roomAmenities:
                filtered_hotels=filtered_hotels.filter(room_amenity__name=roomAmenity)
        print(filtered_hotels)
        hotels_count = filtered_hotels.count()
        hotel_count_for_each_page = 5
        page_count = math.ceil(hotels_count/hotel_count_for_each_page)
        page_range = range(1,page_count+1)

        page = data.get('page',1)
        print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBB',page)
        if isinstance(page, str) and page.isdigit():
            page = int(page)
        hotels_for_each_page = filtered_hotels[(page-1)*5:page*5]
        serializered_hotels = HotelSerializer(hotels_for_each_page,many=True)
        return Response({
            'filtered_hotels': serializered_hotels.data,
            'page_range': page_count,
        })


class GetUserView(APIView):
    def get(self, request):
        data = request.GET
        idForProfile= data.get('userId')
        idForReservation = data.get('reservation-user-id')
        idForHotel = data.get('hotel-user-id')
        if idForProfile:
            user = User.objects.filter(id=idForProfile).first()
            serializered_user = UserSerializer(user)
            data={
                'user': serializered_user.data,
            }
        if idForReservation:
            reservations = Reservation.objects.filter(user__id=idForReservation)
            print(reservations)
            serializered_reservations = ReservationSerializer(reservations,many=True)
            data={
                'reservations': serializered_reservations.data,
            }
        if idForHotel:
            print('hereeeeeeeeee',idForHotel)
            hotels = SavedArticle.objects.filter(user__id=idForHotel)
            serializered_hotels = SavedArticleSerializer(hotels,many=True)
            data={
                'hotels': serializered_hotels.data,
            }
        return Response(data)
