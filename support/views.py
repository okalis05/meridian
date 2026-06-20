from django.shortcuts import render

def index(request):
    # Main page for the Support module.
    return render(request, 'support/index.html', {'title': 'Support', 'desc': 'Support tickets and service requests.'})
