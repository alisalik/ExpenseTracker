from rest_framework import serializers
from tracker.models import Expense
from accounts.models import UserProfile
from accounts.serializers import UserSerializer

class ExpenseSerializer(serializers.ModelSerializer):
    balance=serializers.ReadOnlyField()
    owner=serializers.ReadOnlyField()

    class Meta:
        model = Expense
        fields=['amount','label','credit','debit','owner','balance']

class detailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields=['amount','label','credit','debit','owner','balance']
