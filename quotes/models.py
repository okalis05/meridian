from django.db import models

class Quote(models.Model):
    # A quote captures corporate buying intent before payment.
    company = models.CharField(max_length=160)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    product = models.CharField(max_length=160, blank=True)
    quantity = models.PositiveIntegerField(default=100)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.company} - {self.product}'
