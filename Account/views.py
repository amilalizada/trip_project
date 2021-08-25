from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView

from Account.forms import *
from Account.models import *
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from Account.tools.token import account_activation_token
from django.contrib.auth.mixins import LoginRequiredMixin
from Account.tasks import send_confirmation_email
from django.contrib.auth import get_user_model
from django.shortcuts import redirect



User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
                   
        user = form.save(commit=False)
        user.is_active=False
        user.save()
        site_address = get_current_site(self.request).domain
        print('2----------------------------------------------',user,user.id)
        send_confirmation_email(user.id , site_address)
       
        messages.success(self.request, 'Istifadeci yaradildi')
        return redirect(reverse_lazy('account:login'))



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('account:login')
    messages.error(request,'Activation link is invalid!')    
    return redirect('account:register')


class CustomLoginView(LoginView):
    form_class = MyUserLoginForm
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    form_class =CustomPasswordChangedForm
    template_name = "change-password.html"
    success_url = reverse_lazy('account:login')



class ForgetPasswordView(PasswordResetView):
    email_template_name = 'email/password_reset_email.html'
    template_name = 'forget_password.html'
    success_url = reverse_lazy('account:login')
    form_class = CustomPasswordResetForm

    def form_valid(self, form):
        messages.success(self.request, 'password deyisilmesi ucun sizin mail-e mesaj gonderildi!')
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset-password.html'
    success_url = reverse_lazy('account:login')
    form_class = ResetPasswordForm

    def form_valid(self, form):
        messages.success(self.request, 'password deyisdirildi')
        return super().form_valid(form)

