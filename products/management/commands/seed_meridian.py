
from django.core.management.base import BaseCommand
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Seed starter categories and promotional products.'
    def handle(self, *args, **kwargs):
        names = ['Apparel', 'Drinkware', 'Technology', 'Awards', 'Corporate Gifts']
        for name in names:
            cat, _ = Category.objects.get_or_create(name=name, slug=name.lower().replace(' ', '-'))
            Product.objects.get_or_create(category=cat, name=f'Premium {name} Collection', slug=f'premium-{cat.slug}', defaults={'price': 99, 'description': 'Executive promotional product collection.'})
        self.stdout.write(self.style.SUCCESS('Meridian starter data created.'))
