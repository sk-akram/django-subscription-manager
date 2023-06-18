import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Subscription.settings')

# Configure Django settings
django.setup()


# from subscription_app.views import get_all_subscriptions
# print(get_all_subscriptions())
from subscription_app.models import subscriptionModel

subscriptions = subscriptionModel.objects.all()
for sub in subscriptions:
    print(sub.name, sub.email)
    #Here you can add the smtp email module
    #or you could add twilio api for mobile msg
    #you can save the data to spreadsheet using google sheet api
    #where you can connect it with a server to run every day for newsletter


