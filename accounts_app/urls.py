from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/send_email' , SendEmailView.as_view(), name='news_send_email'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'), 
    path('password-reset/done', ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),  
]