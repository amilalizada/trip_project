
from django import template
from Main.forms import SubscriberForm
from Main.models import StaticPage
register = template.Library()


@register.simple_tag
def get_subscriber_form():
    return SubscriberForm

@register.simple_tag
def get_privacy_terms():
    privacy = StaticPage.objects.get()
    context = {
        'privacy': privacy
    }
    return context

