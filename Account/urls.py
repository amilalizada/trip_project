from django.urls import path, re_path
from Account.views import RegisterView,CustomLoginView , CustomPasswordChangeView , CustomPasswordResetConfirmView ,activate , ForgetPasswordView
from django.contrib.auth.views import LogoutView
app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('activate/<uidb64>/<token>/', activate, name='activation'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name = 'password-reset-confirm'),
    path('change-password/', CustomPasswordChangeView.as_view(), name = 'change_password'),
    path('forget-password/', ForgetPasswordView.as_view(), name='forget_password'), 
    path('logout/', LogoutView.as_view(), name='logout'),
]