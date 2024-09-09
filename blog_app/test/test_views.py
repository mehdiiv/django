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
        
    def test_news_list_view(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/list.html')
        self.assertContains(response, self.news.writer)
    
    def test_news_list_view_logout_auth_user(self):
        logout_client = Client()
        response = logout_client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 302)
    
    def test_news_detail_view(self):
        response = self.client.get(reverse('news_detail', kwargs={ 'pk': self.news.id }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/detail.html')
        self.assertContains(response, self.news.writer)
    
    def test_news_detail_view_logout_auth_user(self):
        logout_client = Client()
        response = logout_client.get(reverse('news_detail', kwargs={ 'pk': self.news.id }))
        self.assertEqual(response.status_code, 302)
    
    def test_news_create_view(self):
        response = self.client.post(reverse('news_create'),{ 'writer' : 'samplpwriter', 'email' : 'sample@examp.com' ,
                                                            'title' : 'sampletitle' , 'descript' : 'sampledescrip', 'country' : 'samplecounrty'

        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(News.objects.filter(writer = 'samplpwriter').exists())
    
    def test_new_update_view(self):
        response = self.client.post(reverse('news_update', kwargs={ 'pk': self.news.id }), { 'writer' : 'samplpwriter', 'email' : 'update@examp.com' ,
                                                            'title' : 'sampletitle' , 'descript' : 'sampledescrip', 'country' : 'samplecounrty'
            
        })
        self.assertEqual(response.status_code, 302)
        self.news.refresh_from_db()
        self.assertEqual(self.news.email, 'update@examp.com')
    
    def test_login_view(self):
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))