from django.shortcuts import render
from .models import subscriptionModel
# Create your views here.

def home(request):
    return render(request, 'home.html')

def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subscription = subscriptionModel(name=name, email=email)
        subscription.save()
        return render(request, 'success.html')
    return render(request, 'home.html')


# def get_all_subscriptions():
#     subscriptions = subscriptionModel.objects.all()
#     return subscriptions