from django import forms
from Main.models import Subscriber,Contact

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )

        widgets = {
            'email': forms.EmailInput(attrs={
                'class':'form-control w-100 py-4 col-md-10 rounded',

                'placeholder':'Enter email address'
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )
        widgets = {
            'name':forms.TextInput(attrs={
                    'class':'form-control py-4',
                     'placeholder':'Your name',
                }),
            'email':forms.TextInput(attrs={
                    'class':'form-control py-4',
                     'placeholder':'Your email',
                }),
            'subject':forms.TextInput(attrs={
                    'class':'form-control py-4',
                     'placeholder':'Subject',
                }),
            'message':forms.Textarea(attrs={
                    'class':'form-control py-4',
                    'rows':7,
                    'cols':30,
                     'placeholder':'Message',
                    'style':'resize:off',
                }),
        }