from django.test import TestCase
from blog_app.models import News

class NewsModelTest(TestCase):
    def setUp(self):
        self.news = News.objects.create(
                writer = 'samplpwriter',
                email = 'sample@examp.com',
                title = 'sampletitle',
                descript = 'sampledescrip',
                country = 'samplecounrty',                        
        )

    def test_news_creation(self):
        self.assertEqual(self.news.writer, 'samplpwriter')
        self.assertEqual(self.news.email, 'sample@examp.com')
        self.assertEqual(self.news.title, 'sampletitle')
        self.assertEqual(self.news.descript, 'sampledescrip')
        self.assertEqual(self.news.country, 'samplecounrty')
        
    def test_news_table_name(self):
        self.assertEqual(self.news._meta.db_table, 'news')