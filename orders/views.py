from django.shortcuts import render

def index(request):
    # Main page for the Orders module.
    return render(request, 'orders/index.html', {'title': 'Orders', 'desc': 'Corporate ordering workflow.'})
