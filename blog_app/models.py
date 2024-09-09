from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    title = models.CharField(max_length=64)
    descript = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news'