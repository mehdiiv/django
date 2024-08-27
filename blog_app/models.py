from django.db import models

class News(models.Model):
    writer = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    descript = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news'