from django.template import Library
from Restaurants.models import Restaurants, RestaurantImages, ToEatReason, RestaurantMenuImages, ReviewRestaurant
from Restaurants.forms import ReviewForm
from django.db.models import Sum, F
from django.db.models.expressions import Window
from django.db.models.functions import Rank
register = Library()

@register.simple_tag
def countRestaurants():
    restaurant = Restaurants.objects.filter(is_published = 'True').count()
    context = {
        'restaurant' : restaurant, 
    }
    return context

@register.simple_tag
def countRestaurantsCity(city,id):
    count = Restaurants.objects.filter(is_published='True',city__name=city).count()
    near_by_restaurants = Restaurants.objects.filter(is_published='True',city__name=city).exclude(id=id)[:4]
    context = {
        'count' : count,
        'near_by_restaurants' : near_by_restaurants,
    }
    return context

@register.simple_tag
def images_count(id):
    count = RestaurantImages.objects.filter(is_published='True',restaurant__id=id).count()
    return count

@register.simple_tag
def images(id):
    all_images = RestaurantImages.objects.filter(is_published='True',restaurant__id=id)
    return all_images

@register.simple_tag
def reason_to_eat(id):
    reasons = ToEatReason.objects.filter(is_published='True',restaurant__id=id)[:3]
    return reasons

@register.simple_tag
def menu_images(id):
    images = RestaurantMenuImages.objects.filter(is_published='True',restaurant__id=id)
    return images

@register.simple_tag
def restaurant_place(id,city):
    place=1
    ordering = Restaurants.objects.filter(is_published='True',city__name=city).order_by('-overall_rating','-review_count')
    for item in ordering:
        if item in Restaurants.objects.filter(is_published='True',id=id):
            break
        place += 1
    return place

@register.simple_tag
def restaurant_place_all(id):
    place=1
    ordering = Restaurants.objects.filter(is_published='True').order_by('-overall_rating','-review_count')
    for item in ordering:
        if item in Restaurants.objects.filter(is_published='True',id=id):
            break
        place += 1
    return place

@register.simple_tag
def review_restaurant(id):
    reviews = ReviewRestaurant.objects.filter(is_published='True',restaurant__id=id)
    reviews_count = ReviewRestaurant.objects.filter(is_published='True',restaurant__id=id).count()
    context = {
        'reviews' : reviews,
        'reviews_count' : reviews_count,
    }
    return context

@register.simple_tag
def review_overall(food,service,value,atmosphere):
    star_html = ''
    star_count = (int(food)+int(service)+int(value)+int(atmosphere))/4
    for i in range(int(float(star_count))):
        star_html = star_html + '<span class="fa fa-star checked"></span>'
    for i in range(int(5-float(star_count))):
        star_html = star_html + '<span class="fa fa-star"></span> '
    if float(star_count) != int(star_count):
        star_html = star_html + '<span class="fa fa-star"></span> '
    return star_html    

@register.simple_tag
def review_part(id):
    review = Restaurants.objects.filter(is_published='True',id=id).first()
    print(review.name)
    star_html_food = ''
    star_html_service = ''
    star_html_value = ''
    star_html_atmosphere = ''
    star_html_all = ''
    for i in range(int(float(review.food_rating ))):
        star_html_food = star_html_food + '<span class="fa fa-star checked"></span>'
    for i in range(int(5-float(review.food_rating ))):
        star_html_food = star_html_food + '<span class="fa fa-star"></span>'
    if float(review.food_rating) != int(review.food_rating):
        star_html_food = star_html_food + '<span class="fa fa-star"></span> '
    
    for i in range(int(float(review.service_rating))):
        star_html_service = star_html_service + '<span class="fa fa-star checked"></span>'
    for i in range(int(5-float(review.service_rating ))):
        star_html_service= star_html_service + '<span class="fa fa-star"></span>'
    if float(review.service_rating) != int(review.service_rating):
        star_html_service = star_html_service + '<span class="fa fa-star"></span> '

    for i in range(int(float(review.value_rating ))):
        star_html_value= star_html_value + '<span class="fa fa-star checked"></span>'
    for i in range(int(5-float(review.value_rating ))):
        star_html_value = star_html_value + '<span class="fa fa-star"></span>'
    if float(review.value_rating ) != int(review.value_rating ):
        star_html_value = star_html_value + '<span class="fa fa-star"></span> '

    for i in range(int(float(review.atmosphere_rating ))):
        star_html_atmosphere = star_html_atmosphere + '<span class="fa fa-star checked"></span>'
    for i in range(int(5-float(review.atmosphere_rating))):
        star_html_atmosphere = star_html_atmosphere + '<span class="fa fa-star"></span>'
    if float(review.atmosphere_rating) != int(review.atmosphere_rating):
        star_html_atmosphere = star_html_atmosphere + '<span class="fa fa-star"></span> '

    for i in range(int(float(review.overall_rating))):
        star_html_all = star_html_all + '<span class="fa fa-star checked"></span>'
    for i in range(int(5-float(review.overall_rating))):
        star_html_all = star_html_all + '<span class="fa fa-star"></span>'
    if float(review.overall_rating) != int(review.overall_rating):
        star_html_all = star_html_all + '<span class="fa fa-star"></span> '
    
    if review.overall_rating != int(review.overall_rating):
        review.overall_rating = str(int(review.overall_rating))+'.0'
        review.overall_rating = float(review.overall_rating)

    context = {
        'star_html_food' : star_html_food,
        'star_html_service' : star_html_service,
        'star_html_value' : star_html_value,
        'star_html_atmosphere' : star_html_atmosphere,
        'star_html_all' : star_html_all,
        'star_html_all_count' : review.overall_rating,
    }

    return context  

@register.simple_tag
def get_review_form():  
    return ReviewForm()

