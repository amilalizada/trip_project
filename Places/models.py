from django.db import models
from Main.models import City
from Account.models import User


def upload_location(instance,filename):
    return 'images/places/%s/images/%s' %(instance.place,filename)

def video_upload_location(instance,filename):
    return 'images/places/%s/video/%s' %(instance.place,filename)

def menu_upload_location(instance,filename):
    return 'images/places/%s/menu/%s' %(instance.name,filename)

class OptionsPlaces(models.Model):
    input_type_choice = [
        ('radio', 'radio'),
        ('checkbox', 'checkbox'),
    ]
    option_name = models.CharField('Option Name',max_length=120)
    option_svg_file = models.ImageField('Svg file',upload_to='images/places/svg-files')
    option_input_type = models.CharField('Input type',max_length=10,choices=input_type_choice)
    option = models.CharField('Option',max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
    
    def __str__(self):
        return self.option

class Places(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True, related_name='user_place')
    name = models.CharField('Name',max_length=40)
    city = models.ForeignKey(City, on_delete = models.CASCADE,db_index=True, related_name = 'city_name_place')
    options = models.ManyToManyField(OptionsPlaces, verbose_name='Options', related_name='options_place')
    image = models.ImageField('Image',upload_to=upload_location)
    video = models.FileField('Video',upload_to=video_upload_location)
    location = models.CharField('Location',max_length=250)
    open_time = models.CharField('Open Time',max_length=250)
    description = models.TextField('Description')
    special_diets = models.CharField('Special Diets',max_length = 240)
    features = models.CharField('Features',max_length=500)


    
    # Top 3 reasons to go there
    reason_one = models.CharField('Reason 1', max_length=50)
    reason_one_img = models.ImageField('Reason 1 image',upload_to=upload_location)
    reason_one_short_description = models.CharField('Reason 1 description',max_length=60)
    reason_two = models.CharField('Reason 2', max_length=50)
    reason_two_img = models.ImageField('Reason 2 image',upload_to=upload_location)
    reason_two_short_description = models.CharField('Reason 2 description',max_length=60)
    reason_three = models.CharField('Reason 3', max_length=50)
    reason_three_img = models.ImageField('Reason 3 image',upload_to=upload_location)
    reason_three_short_description = models.CharField('Reason 3 description',max_length=60)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
    
    def __str__(self):
        return self.name
    

class PlaceImages(models.Model):
    place = models.ForeignKey(Places,on_delete=models.CASCADE, db_index=True, related_name='name_place')
    images = models.ImageField('Image',upload_to=upload_location)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Place_image'
        verbose_name_plural = 'Places_images'
    
    def __str__(self):
        return self.place

# Create your models here.
