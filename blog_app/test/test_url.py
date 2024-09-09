from django.test import SimpleTestCase
from blog_app.views import (
    NewsDetailView, NewsListView,
    NewsUpdateView, NewsDeleteView,
   NewsCreateView
)
from django.urls import resolve, reverse

class UrlTest(SimpleTestCase):

    def test_news_list_url(self):
        url = reverse('news_list')
        self.assertEqual(resolve(url).func.view_class, NewsListView)
    
    def test_news_create_url(self):
        url = reverse('news_create')
        self.assertEqual(resolve(url).func.view_class, NewsCreateView)
    
    def test_news_detail_url(self):
        url = reverse('news_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, NewsDetailView)
    
    def test_news_update_url(self):
        url = reverse('news_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, NewsUpdateView)
    
    def test_news_delete_url(self):
        url = reverse('news_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, NewsDeleteView)
    
