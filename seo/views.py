from django.shortcuts import render

def index(request):
    # Main page for the Seo module.
    return render(request, 'seo/index.html', {'title': 'Seo', 'desc': 'SEO metadata, sitemap helpers, and landing pages.'})
