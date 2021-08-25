from django.db import models
from Main.models import City
from Account.models import User
from Main.tools.slug_generator import slugify
from django.urls import reverse_lazy
from datetime import datetime
from django.db.models import Sum

def upload_location(instance,filename):
    return 'images/restaurants/%s/images/%s' %(instance.name,filename)

def video_upload_location(instance,filename):
    return 'images/restaurants/%s/video/%s' %(instance.name,filename)

def menu_upload_location(instance,filename):
    return 'images/restaurants/%s/menu/%s' %(instance.restaurant.name,filename)

def upload_location_restaurant_image(instance,filename):
    return 'images/restaurants/%s/images/%s' %(instance.restaurant.name,filename)


class OptionListTypeCheckbox(models.Model):
    option_name = models.CharField('Option',max_length=120)

    class Meta:
        verbose_name = 'Option List Type Checkbox'
        verbose_name_plural = 'Option Lists Type Checkbox'
    
    def __str__(self):
        return self.option_name

class OptionsTypeCheckbox(models.Model):
    option_name = models.CharField('Option Name',max_length=120)
    option_svg_file = models.FileField('Svg file',upload_to='images/restaurants/svg-files')
    option_inputs =  models.ManyToManyField(OptionListTypeCheckbox, verbose_name='Options', related_name='input_restaurant_checkbox')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Option Type Checkbox'
        verbose_name_plural = 'Options Type Checkbox'
    
    def __str__(self):
        return self.option_name

class OptionListTypeRadio(models.Model):
    option_name = models.CharField('Option',max_length=120)

    class Meta:
        verbose_name = 'Option List Type Radio'
        verbose_name_plural = 'Option Lists Type Radio'
    
    def __str__(self):
        return self.option_name

class OptionsTypeRadio(models.Model):
    option_name = models.CharField('Option Name',max_length=120)
    option_svg_file = models.FileField('Svg file',upload_to='images/restaurants/svg-files')
    option_inputs =  models.ManyToManyField(OptionListTypeRadio,verbose_name='Option',related_name='input_restaurant_radio')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Option Type Radio'
        verbose_name_plural = 'Options Type Radio'
    
    def __str__(self):
        return self.option_name

class Restaurants(models.Model):
    rating_type_choice = [
        ('0.5', '0.5'),
        ('1.0', '1.0'),
        ('1.5', '1.5'),
        ('2.0', '2.0'),
        ('2.5', '2.5'),
        ('3.0', '3.0'),
        ('3.5', '3.5'),
        ('4.0', '4.0'),
        ('4.5', '4.5'),
        ('5.0', '5.0'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True, related_name='user_restaurant')
    

    name = models.CharField('Name',max_length=40)

    city = models.ForeignKey(City, on_delete = models.CASCADE,db_index=True, related_name = 'city_name_restaurant')
    checkbox_options = models.ManyToManyField(OptionListTypeCheckbox, verbose_name='Options', related_name='options_restaurant_checkbox')
    radio_options = models.ForeignKey(OptionListTypeRadio,on_delete = models.CASCADE,db_index=True,related_name='options_restaurant_radio')
    image = models.ImageField('Main Image',upload_to=upload_location)
    image_second = models.ImageField('Second Image',upload_to=upload_location)
    image_third = models.ImageField('Third Image',upload_to=upload_location)
    phone_number = models.CharField('Phone Number',max_length=40)
    video = models.FileField('Video',upload_to=video_upload_location)
    website = models.CharField('Website',max_length=250)
    location = models.CharField('Location',max_length=250)
    location_link = models.CharField('Location URL',max_length=250)
    open_time = models.TimeField('Open Time')
    close_time = models.TimeField('Close Time')
    description = models.TextField('Description')
    min_price = models.IntegerField('Min Price')
    max_price = models.IntegerField('Max Price')
    special_diets = models.CharField('Special Diets',max_length = 240)
    meals = models.CharField('Meals',max_length = 240)
    cuisines = models.CharField('Cuisines',max_length=40)
    features = models.CharField('Features',max_length=500)
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)
    food_rating = models.DecimalField('Food_rating',max_digits=2, decimal_places=1,blank=True, null=True)
    service_rating = models.DecimalField('Service_rating',max_digits=2, decimal_places=1,blank=True, null=True)
    value_rating = models.DecimalField('Value_rating',max_digits=2, decimal_places=1,blank=True, null=True)
    atmosphere_rating = models.DecimalField('Atmosphere_rating',max_digits=2, decimal_places=1,blank=True, null=True)
    overall_rating = models.DecimalField('Overall Rating',max_digits=2,decimal_places=1,blank=True,null=True)
    review_count = models.IntegerField('Count Reviews',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)



    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse_lazy('restaurants_app:restaurant_single_page', kwargs={'slug': self.slug }) 

    

class RestaurantImages(models.Model):
    restaurant = models.ForeignKey(Restaurants,on_delete=models.CASCADE, db_index=True, related_name='name_restaurant')
    images = models.ImageField('Image',upload_to=upload_location_restaurant_image)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Restaurant_image'
        verbose_name_plural = 'Restaurants_images'
    
    def __str__(self):
        return self.restaurant.name

class RestaurantMenuImages(models.Model):
    restaurant = models.ForeignKey(Restaurants,on_delete=models.CASCADE, db_index=True, related_name='menu_restaurant')
    images = models.ImageField('Image Menu',upload_to=menu_upload_location)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Restaurant_menu_image'
        verbose_name_plural = 'Restaurants_menu_images'
    
    def __str__(self):
        return self.restaurant.name




class ToEatReason(models.Model):
    rating_type_choice = [
        ('0.5', '0.5'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    ]
    restaurant = models.ForeignKey(Restaurants,on_delete=models.CASCADE, db_index=True, related_name='eat_reason_restaurant')
    reason = models.CharField('Reason ', max_length=50)
    reason_img = models.ImageField('Reason image',upload_to=upload_location_restaurant_image)
    reason_rating = models.CharField('Rating',max_length=10,choices=rating_type_choice)
    reason_short_description = models.CharField('Reason description',max_length=60)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'To Eat Reason'
        verbose_name_plural = 'To Eat Reasons'
    
    def __str__(self):
        return self.restaurant.name

class ReviewRestaurant(models.Model):
    rating_type_choice = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    user = user = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True, related_name='user_restaurant_review')
    restaurant = models.ForeignKey(Restaurants,on_delete=models.CASCADE, db_index=True, related_name='review_restaurant')
    comment = models.TextField('Comment')
    food_rating = models.CharField('Food',max_length=10,choices=rating_type_choice)
    service_rating = models.CharField('Service',max_length=10,choices=rating_type_choice)
    value_rating = models.CharField('Value',max_length=10,choices=rating_type_choice)
    atmosphere_rating = models.CharField('Atmosphere',max_length=10,choices=rating_type_choice)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)


    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return self.restaurant.name

    def save_star(self):
        obj = ReviewRestaurant.objects.filter(is_published='True',restaurant__name=self.restaurant.name)
        count = ReviewRestaurant.objects.filter(is_published='True',restaurant__name=self.restaurant.name).count()
        ratings_food = 0
        ratings_services = 0
        ratings_value = 0
        ratings_atmosphere = 0
        for item in obj:
            print(item)
            ratings_food += int(item.food_rating)
            ratings_services += int(item.service_rating)
            ratings_value += int(item.value_rating)
            ratings_atmosphere += int(item.atmosphere_rating)
        self.restaurant.food_rating = ratings_food/count
        self.restaurant.service_rating = ratings_services/count
        self.restaurant.value_rating = ratings_value/count
        self.restaurant.atmosphere_rating = ratings_atmosphere/count
        self.restaurant.overall_rating = (self.restaurant.food_rating + self.restaurant.service_rating + self.restaurant.value_rating + self.restaurant.atmosphere_rating)/4
        self.restaurant.review_count = count
        self.restaurant.save()

class SavedArticleRestaurants(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True, related_name='restaurant_saved_articles',)
    restaurant =models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name='restaurant_saved_articles', null=True, blank=True)
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Saved Article'
        verbose_name_plural = 'Saved Articles'
    def __str__(self):
        return f"{self.user} tour: {self.restaurant.name}"





# Create your models here.
