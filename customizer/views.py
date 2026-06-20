from django.shortcuts import render

def index(request):
    # Main page for the Customizer module.
    return render(request, 'customizer/index.html', {'title': 'Customizer', 'desc': 'Product customization studio.'})
