from django.shortcuts import render

def index(request):
    # Main page for the Customers module.
    return render(request, 'customers/index.html', {'title': 'Customers', 'desc': 'Customer portal and saved company profiles.'})
