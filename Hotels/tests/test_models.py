from django.test import TestCase
from Hotels.models import Hotel,City,User,Policies,RoomType,HotelAmenities,RoomAmenities,ReviewFields
from django.core.files import File


class HotelTestCase(TestCase):

    def setUp(self):
        self.model_data = {
            'name': 'HOtel First',
            'name_description': 'Best hotel',
            'short_description':'Fantastico',
            'long_description':'The best hotel',
            'longitude':'50',
            'latitude':'50',
            'phone_number':'555555',
            'website':'first.com',
            'rating':'5',
            'main_image':File(open("/home/aqil/Desktop/docker_group_trip_project_final/media/images/baku1.jpg")),
            'min_price':'50',
            'city':City.objects.all().first(),
            'author':User.objects.all().first(),
            'policies':Policies.objects.all()[:2],
            'room_type':RoomType.objects.all(),
            'hotel_amenity':HotelAmenities.objects.all(),
            'room_amenity':RoomAmenities.objects.all(),
            'review_fields':ReviewFields.objects.all(),
        }
        self.content = Hotel.objects.create(**self.model_data)


    def test_created_data(self):
        hotel_data = Hotel.objects.all()[0]
        self.assertEqual(hotel_data,self.content)

    # def test_str_method(self):
    #     expected_result = f'{self.content.name} subject:{self.content.subject}'
    #     self.assertEqual(expected_result,self.content.__str__())
    #
    # def test_get_email_method(self):
    #     expected_result = self.content.get_email()
    #     self.assertEqual(expected_result,self.content.get_email())
    #
    # def tearDown(self):
    #     Hotel.objects.filter(id__in=[self.content.id]).delete()