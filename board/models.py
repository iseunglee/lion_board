from django.db import models
from board.fields import ThumbnailImageField

# Create your models here.
class Category(models.Model):
    ct_name = models.CharField(max_length=30)

    
    
class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    it_name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')

