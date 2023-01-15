from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length = 50)
    extra_inf = models.TextField()
    price = models.IntegerField()
    post_date = models.DateTimeField(auto_now_add =True)
