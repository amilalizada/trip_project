from django.db import models
from django.contrib.auth import get_user_model
from Main.models import City
from tools.slug_generator import slugify
from django.urls import reverse_lazy
from datetime import datetime
from django.core.paginator import Paginator
USER_MODEL = get_user_model()

class Tours(models.Model):

    #relations
    owner = models.ForeignKey(USER_MODEL, related_name='tur', on_delete=models.CASCADE)
    city = models.ManyToManyField(City, verbose_name='City', related_name='tours')

    name = models.CharField('Basligi', max_length=120)
    trip_route = models.CharField('Yol',max_length=1000)
    trip_time = models.CharField('Vaxt',max_length=1000)
    trip_time_count = models.IntegerField('Gun sayi', blank=True , null=True)  
    trip_transport = models.CharField('Neqliyyat',max_length=200)
    price = models.DecimalField('Qiymet',max_digits=6, decimal_places=2)
    main_image = models.ImageField('Main image',upload_to='images/tourimages')
    strat = models.CharField('Baslanma yeri', max_length=100) 
    finish = models.CharField('Bitme yeri' , max_length=100)
    min_size = models.IntegerField('Minumum adam sayi',blank=True , null=True)
    max_size = models.IntegerField('Maksimum adam sayi',blank=True , null=True)
    min_age = models.IntegerField('Minumum yash',blank=True , null=True)
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)


    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta():
        verbose_name = 'Tur'
        verbose_name_plural = 'Turlar'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.name}" 

    def save(self,*args, **kwargs):
        
        name = self.name
        self.slug = f"{slugify(self.name)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()
    
    def get_absolute_url(self):
        return reverse_lazy('tours:tour-detail', kwargs={'slug': self.slug})

class TourComments(models.Model):

    # relations
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.ForeignKey(USER_MODEL, related_name='comments', on_delete=models.CASCADE)

    # website = models.URLField('Website', null=True, blank=True)
    content = models.TextField('Content')

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)



    def __str__(self):
        return self.content


class TourImages(models.Model):

    # relations
    tours  = models.ForeignKey(Tours, on_delete=models.CASCADE , db_index=True , related_name="tour_images")

    images = models.ImageField('Images' , upload_to="images/tours/tourimages")
    

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Inclusion(models.Model):
    tours  = models.OneToOneField(Tours, on_delete=models.CASCADE , db_index=True , related_name="inclusion")

    meals = models.CharField('Yemekler', max_length=120)
    transport = models.CharField('Neqliyyat', max_length=250) 
    acommodation = models.CharField('Qonaqlama',max_length=120)
    




class WhyYouLove(models.Model):
    tours  = models.ForeignKey(Tours, on_delete=models.CASCADE , db_index=True , related_name="whyyoulove")

    reasons = models.CharField('Sebebler' , max_length=1000)

class RightRorYou(models.Model):
    tours  = models.ForeignKey(Tours, on_delete=models.CASCADE , db_index=True , related_name="rightforyou")

    will_do = models.CharField('Edeceklerimiz', max_length=1500)

class ImportantNotes(models.Model):
    tours  = models.ForeignKey(Tours, on_delete=models.CASCADE , db_index=True , related_name="notes")

    note_title = models.CharField('Not bashligi', max_length=1000)
    notes = models.CharField('Qeydler',max_length=1000)

class Activites(models.Model):
    inclusion  = models.ForeignKey(Inclusion, on_delete=models.CASCADE , db_index=True , related_name="activities")
    
    avtivity = models.TextField('Eylence')



class SavedArticleTour(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, related_name='tour_saved_articles',)
    tour =models.ForeignKey(Tours, on_delete=models.CASCADE, related_name='tour_saved_articles', null=True, blank=True)
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Saved Article'
        verbose_name_plural = 'Saved Articles'
    def __str__(self):
        return f"{self.user} tour: {self.tour.name}"