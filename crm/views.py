from django.shortcuts import render

def index(request):
    # Main page for the Crm module.
    return render(request, 'crm/index.html', {'title': 'Crm', 'desc': 'Lead and client relationship tracking.'})
