from django.shortcuts import render


def advisor(request):
    # Starter AI advisor. Later connect to OpenAI or another approved model.
    idea = request.GET.get('idea', '')
    reply = 'Tell me the audience, budget, quantity, and deadline to receive polished product recommendations.'
    if idea:
        reply = f'Executive recommendation for {idea}: start with premium drinkware, embroidered apparel, and a boxed corporate gift set.'
    return render(request, 'ai_tools/index.html', {'title': 'AI Product Advisor', 'reply': reply})
