from django.shortcuts import render

def index(request):
    # Main page for the Analytics module.
    return render(request, 'analytics/index.html', {'title': 'Analytics', 'desc': 'Executive analytics dashboard.'})
