from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
        category = models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        description = models.TextField(blank=True, null=True)
        price = models.FloatField()
        #image = models.ForeignKey(ItemPhoto, related_name='items', on_delete=models.CASCADE)
        is_sold = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
        

        class Meta:
            ordering = ('name',)
            verbose_name_plural = 'Items'
    
        def __str__(self):
            return self.name
        

class ItemPhoto(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return f"Photo for {self.item.name}"
