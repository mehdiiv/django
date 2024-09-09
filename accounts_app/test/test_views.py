from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from blog_app.models import News
from django.contrib.auth.models import User

class NewsViewTest(TestCase):
    def setUp(self):
        self.news = User.objects.create_user(username='test', password='1223234')
        self.client = Client()
        self.client.login(username='test', password='1223234')

        self.news = News.objects.create(writer = 'samplpwriter', email = 'sample@examp.com' ,
                                        title = 'sampletitle' , descript = 'sampledescrip', country = 'samplecounrty')
        
    def test_login_view(self):
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))