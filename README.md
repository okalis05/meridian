
# FEO Meridian Brands — Enterprise Django Starter

This project is named `meridian` and is built for **FEO MERIDIAN BRANDS LLC**, a premium promotional products business serving companies, organizations, and corporations.

## Included apps
core, products, customizer, quotes, orders, customers, ai_tools, dealer, payments, seo, analytics, blog, accounts, crm, support, notifications.

## Run locally
```bash
cd meridian_enterprise
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_meridian
python manage.py runserver
```

## Important security note
Kaeser & Blair dealer login is linked through `KAESER_BLAIR_DEALER_URL`. Do not store your dealer username or password in Django code.

## Design standard
Executive glassmorphism with charcoal, metallic gold, white, and crimson accents.
