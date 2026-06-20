from django.shortcuts import render

def index(request):
    # Main page for the Blog module.
    return render(request, 'blog/index.html', {'title': 'Blog', 'desc': 'Blog and CMS pages.'})
