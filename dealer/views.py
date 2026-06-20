from django.shortcuts import render


from django.conf import settings
def dealer_home(request):
    # Never store your Kaeser & Blair password in code. Link securely to the dealer portal.
    return render(request, 'dealer/index.html', {'title': 'Kaeser & Blair Layer', 'dealer_url': settings.KAESER_BLAIR_DEALER_URL})
