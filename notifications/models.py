from django.db import models

class EmailLog(models.Model):
    # Email event log for quote, order, and support notifications.
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.subject
