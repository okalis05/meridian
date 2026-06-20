
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('products.urls')),
    path('customizer/', include('customizer.urls')),
    path('quotes/', include('quotes.urls')),
    path('orders/', include('orders.urls')),
    path('portal/', include('customers.urls')),
    path('ai/', include('ai_tools.urls')),
    path('dealer/', include('dealer.urls')),
    path('payments/', include('payments.urls')),
    path('seo/', include('seo.urls')),
    path('analytics/', include('analytics.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('crm/', include('crm.urls')),
    path('support/', include('support.urls')),
    path('notifications/', include('notifications.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
