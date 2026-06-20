
from django.shortcuts import render

def home(request):
    # Luxury public homepage for FEO Meridian Brands LLC.
    items = ['Custom promotional products', 'Corporate gifts', 'Branded apparel', 'Quote-first B2B ordering', 'AI product advisor', 'Dealer-ready operations']
    return render(request, 'core/home.html', {'items': items})
