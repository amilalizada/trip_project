from celery import shared_task
from django.core.mail import EmailMessage
from Hotels.models import Hotel
from Main.models import Subscriber
from datetime import date,timedelta
from django.template.loader import render_to_string
from django.conf import settings


@shared_task
def send_email_to_subscribers():
    today = date.today()
    yest = today - timedelta(days=1)
    hotels = Hotel.objects.filter(created_at__gte=yest,created_at__lt=today)
    template_name = 'email-subscribers.html'
    context = {
        'hotels':hotels,
        'site_address':settings.SITE_ADDRESS,
    }
    msg = render_to_string(template_name,context)
    subject = 'New Stories'
    user_emails= Subscriber.objects.filter(is_active=True).values_list('email',flat=True)
    message = EmailMessage(subject=subject,body=msg,from_email=settings.EMAIL_HOST_USER,to=user_emails)
    message.content_subtype = 'html'
    message.send()