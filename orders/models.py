from django.db import models

class Order(models.Model):
    # Corporate orders move from draft to paid to fulfilled.
    company = models.CharField(max_length=160)
    email = models.EmailField()
    status = models.CharField(max_length=40, default='draft')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.company} order #{self.id}'
