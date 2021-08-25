from celery import shared_task
from django.shortcuts import render
from django.core.mail import EmailMessage
from Hotels.models import Reservation
from Account.models import User
from datetime import date,timedelta
from django.template.loader import render_to_string
from django.conf import settings
import datetime
import dateutil.parser

# @shared_task
# def send_at_time(email,id,url,fin_date):
#     send_email_to_users.apply_async((email,id,url),eta=fin_date)

@shared_task
def send_email_to_users(email,id,url):
    template_name = 'send_template.html'
    context ={
        'url':url,
        'reservation_id':id,
    }
    subject='Review our hotel'
    msg=render_to_string(template_name,context)
    message = EmailMessage(subject=subject,body=msg, from_email=settings.EMAIL_HOST_USER, to=[email])
    message.content_subtype = 'html'
    message.send()

    # today = date.today()
    # yest = today - timedelta(days=1)
    # recipes = Recipe.objects.filter(created_at__gte=yest,created_at__lt=today)
    # stories = Story.objects.filter(created_at__gte=yest, created_at__lt=today)
    #
    # template_name = 'email-subscribers.html'
    # context = {
    #     'recipes':recipes,
    #     'stories':stories,
    #     'site_address':settings.SITE_ADDRESS,
    # }
    # msg = render_to_string(template_name,context)
    # subject = 'New Stories'
    # user_emails= Subscriber.objects.filter(is_active=True).values_list('email',flat=True)
    # message = EmailMessage(subject=subject,body=msg,from_email=settings.EMAIL_HOST_USER,to=user_emails)
    # message.content_subtype = 'html'
    # message.send()
