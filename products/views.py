from django.shortcuts import render

def index(request):
    # Main page for the Products module.
    return render(request, 'products/index.html', {'title': 'Products', 'desc': 'Promotional product catalog and categories.'})
