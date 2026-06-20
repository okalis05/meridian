from django.db import models

class Ticket(models.Model):
    # Support ticket for customer service requests.
    subject = models.CharField(max_length=180)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=40, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.subject
