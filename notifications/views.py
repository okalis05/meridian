from django.shortcuts import render

def index(request):
    # Main page for the Notifications module.
    return render(request, 'notifications/index.html', {'title': 'Notifications', 'desc': 'Email notification templates and logs.'})
