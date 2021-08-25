from django.db import models
from ckeditor.fields import RichTextField
from Account.models import User
from tools.slug_generator import slugify
from tools.slug_generator import slugify
from django.urls import reverse_lazy
from datetime import datetime
# from django.contrib.auth import get_user_model
# USER_MODEL = get_user_model()

class Contact(models.Model):
    #information
    name = models.CharField('Name',max_length=40)
    email = models.EmailField('Email',max_length=40)
    subject = models.CharField('Subject',max_length=255)
    message = models.TextField('Message')

    # moderation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.name} subject:{self.subject}'

    def get_email(self):
        return self.email

class City(models.Model):
    #relations
   


    #information
    name = models.CharField('Name',max_length=40)
    main_image = models.ImageField('Image',upload_to='images')
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        
        name = self.name
        self.slug = f"{slugify(self.name)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()

    def get_absolute_url(self):
        return reverse_lazy('main:city-detail', kwargs={'slug': self.slug})

    

class Places(models.Model):
    #relations
    city = models.ForeignKey(City,verbose_name='City',on_delete=models.CASCADE,related_name='places')

    #information
    title = models.CharField('Name',max_length=40)
    location = models.CharField('Name',max_length=40)
    image = models.ImageField('Image',upload_to='images')
    description = models.TextField('Description')
    latitude = models.DecimalField('Latitude',max_digits=6,decimal_places=2)
    longtitude = models.DecimalField('Longtitude', max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Places'
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.title

class Helps(models.Model):
    #information
    popular_questions = models.TextField('Popular questions')
    answers = models.TextField('Answers')

    #moderation
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Helps'
        verbose_name_plural = 'Helps'

    def __str__(self):
        return self.popular_questions

class ContactInfo(models.Model):
    #information
    fullname = models.CharField('Fullname',max_length=60)
    email = models.CharField('Email',max_length=40)
    phone_number = models.PositiveIntegerField('Phone Number')
    location = models.CharField('Our location',max_length=100)

    class Meta:
        verbose_name = 'Our Contact'
        verbose_name_plural = 'Our Contacts'

    def __str__(self):
        return self.fullname

class StaticPage(models.Model):
    #information
    terms_of_service = RichTextField('Terms of Service')
    privacy_policy = RichTextField('Privacy Policy')

    #moderation
    # moderation
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_published = models.BooleanField('is published', default=True)

class AboutProject(models.Model):
    #information
    project_devops = models.CharField('Fullname',max_length=60)
    key_words = models.CharField('Key words',max_length=500)
    title = models.CharField('Title',max_length=60)
    faq_icon = models.ImageField('Faq icon',upload_to='images')
    logo = models.ImageField('Logo',upload_to='images')
    description = models.TextField('Description')

    #moderation
    project_developing_start_time = models.DateField()
    project_developing_finish_time = models.DateField()

class WebsiteSettings(models.Model):
    #information
    type_choice = [
        ('az', 'Azerbaijan'),
        ('eng', 'English'),
        ('rus', 'Russian'),
    ]
    languages = models.CharField('Type', max_length=5, choices=type_choice)
    cover_image = models.ImageField('Image',upload_to='image')

class Subscriber(models.Model):
    email = models.EmailField('Email',max_length=30,unique=True)
    is_active = models.BooleanField('is active',default=True)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email


