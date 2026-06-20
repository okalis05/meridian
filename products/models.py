from django.db import models

class Category(models.Model):
    # Simple product category such as Apparel, Drinkware, Tech, or Awards.
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    def __str__(self): return self.name

class Product(models.Model):
    # Product records can be entered manually or synced from a dealer/catalog source.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    def __str__(self): return self.name
