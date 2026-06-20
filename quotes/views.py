from django.shortcuts import render

def index(request):
    # Main page for the Quotes module.
    return render(request, 'quotes/index.html', {'title': 'Quotes', 'desc': 'Quote request and quote management.'})
