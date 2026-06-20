from django.shortcuts import render


def checkout(request):
    # Stripe placeholder. Add Stripe Checkout Session creation after keys are configured.
    return render(request, 'payments/index.html', {'title': 'Stripe Payments', 'message': 'Stripe checkout placeholder is ready for secure API keys.'})
