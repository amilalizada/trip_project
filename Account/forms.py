from django import forms
from Account.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from django.template.loader import render_to_string, get_template
from django.urls import reverse_lazy
from django.core.mail import EmailMessage


class RegisterForm(UserCreationForm):
    name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'name',
                'class' : 'form-control',
                'autofocus': 'autofocus',
            }))

    surname = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'name',
                'class' : 'form-control',
            }))

    username = UsernameField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Username',
                'class' : 'form-control',
            }))

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'placeholder' : 'Email',
                'class' : 'form-control',
            }))

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirm password',
                'class' : 'form-control',
             }))

    class Meta:
        model = User
        fields = ('name', 'surname' ,"username", 'email', 'password1', 'password2', )



class MyUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control pr-55', 'id': 'signin-password','maxlength':'40','placeholder': 'password'}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username__iexact=username).first()
        if user:
            return user.email
        return username.lower()

    error_messages = {
        'invalid_login': 'You have entered an invalid email or password',
    }


class CustomPasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 
        'autofocus': True,
        'class': 'form-control',
        'placeholder': 'Old Password',
        }),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
        'class': 'form-control',
        'placeholder': 'New Password',
            }),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
        'class': 'form-control',
        'placeholder': 'Confirm New Password',
        }),
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'form-control',
            'placeholder': _('Email'),
        })
    )

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        context['redirect_url'] = f"{ context['protocol'] }://{context['domain']}{ reverse_lazy('account:password-reset-confirm' , kwargs = {'uidb64':context['uid'], 'token':context['token']} )}"
        body = render_to_string(email_template_name, context)

        # email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        # if html_email_template_name is not None:
        #     html_email = loader.render_to_string(html_email_template_name, context)
        #     email_message.attach_alternative(html_email, 'text/html')

        # email_message.send()
        
        email = EmailMessage(
                subject, body, to=[to_email]
            )
        email.content_subtype = 'html'
        email.send()

class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
        'class': 'form-control',
        'placeholder': 'New Password',}),
        strip=False,
        help_text=password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
        'class': 'form-control',
        'placeholder': 'New password confirmation',}),
    )