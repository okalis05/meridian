from django.shortcuts import render

def index(request):
    # Main page for the Accounts module.
    return render(request, 'accounts/index.html', {'title': 'Accounts', 'desc': 'Role-based access helpers and user profiles.'})
