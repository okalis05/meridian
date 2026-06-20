from django.contrib import admin
from . import models

# Automatically register simple starter models for fast admin access.
for name in dir(models):
    item = getattr(models, name)
    if hasattr(item, '_meta') and getattr(item._meta, 'app_label', None) == __package__:
        try: admin.site.register(item)
        except admin.sites.AlreadyRegistered: pass
