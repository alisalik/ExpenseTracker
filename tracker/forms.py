from django import forms
from tracker.models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        field="__all__"
        
