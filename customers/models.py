from django.db import models

class CustomerProfile(models.Model):
    # Portal profile for repeat corporate buyers.
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    company = models.CharField(max_length=160)
    phone = models.CharField(max_length=40, blank=True)
    def __str__(self): return self.company
