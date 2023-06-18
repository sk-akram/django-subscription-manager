from django.db import models

# Create your models here.
class subscriptionModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.email
    class Meta:
        app_label ='subscription_app'
