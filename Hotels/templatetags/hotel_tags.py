from django import template
from Hotels.models import Reviews
register = template.Library()


@register.simple_tag
def get_star_count(star_count):
    star_html = ''
    for i in  range(int(star_count)):
        star_html=star_html+'<span class="fa fa-star checked"> </span>'
    for i in range(int(5-star_count)):
        star_html=star_html+'<span class="fa fa-star"></span>'
    return star_html

@register.simple_tag
def get_bed_count(bed_count):
    bed_html = ''
    for i in range(int(bed_count)):
        bed_html = bed_html + '<i class="fas fa-user-alt" style="font-size:20px"></i>'
    return bed_html

@register.simple_tag
def review_count(hotel_id):
    count = Reviews.objects.filter(reservation__hotel__pk=hotel_id).count()
    return count

@register.simple_tag
def reviews(hotel_id):
    review_count=Reviews.objects.filter(reservation__hotel__pk=hotel_id).count()
    if review_count >= 4:
        reviews = Reviews.objects.filter(reservation__hotel__pk=hotel_id)[review_count-4:review_count]
    else:
        reviews=Reviews.objects.filter(reservation__hotel__pk=hotel_id)
    print(reviews)
    return reviews