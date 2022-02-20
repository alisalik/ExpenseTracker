from django.db import models
from accounts.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class Expense(models.Model):
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    balance=models.FloatField(default=0)
    label = models.CharField(max_length=100)
    debit = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)

    '''@property
    def get_balance(self):
        self.balance+=UserProfile.total_income
        return self.balance'''



'''@receiver(post_save, sender=Expense)
def create_balance(sender,instance=None,created=False,**kwargs):
    if created:
        Expense.objects.update_or_create(balance=UserProfile.total_income,owner=UserProfile.name)
        Expense.save()'''
