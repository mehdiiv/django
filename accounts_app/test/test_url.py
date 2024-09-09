from django.test import SimpleTestCase
from accounts_app.views import (SendEmailView, LogoutView ,LoginView)
from django.urls import resolve, reverse

class UrlTest(SimpleTestCase):

    
    def test_send_email_url(self):
        url = reverse('news_send_email', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, SendEmailView)
    

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginView)
    
    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)
