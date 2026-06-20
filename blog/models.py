from django.db import models

class Post(models.Model):
    # SEO-friendly CMS article.
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
