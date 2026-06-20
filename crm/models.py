from django.db import models

class Lead(models.Model):
    # Sales pipeline lead for follow-up.
    company = models.CharField(max_length=160)
    contact = models.CharField(max_length=120)
    email = models.EmailField()
    stage = models.CharField(max_length=60, default='new')
    notes = models.TextField(blank=True)
    def __str__(self): return self.company
