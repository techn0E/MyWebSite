from django import forms
from .models import MyModel, User, Expense, Earning, Budget

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["fullname", "birthday",]
    labels = {'fullname': "Name", "birthday": "birthday",}

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ["username", "password",]
    inputs = {'username': "Name"}

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['product_title', 'user_amount']
        widgets = {
            'product_title': forms.TextInput(attrs={
                'class': 'product-title',
                'placeholder': 'Enter Title of Product'
            }),
            'user_amount': forms.NumberInput(attrs={
                'id': 'user-amount',
                'placeholder': 'Enter Cost of Product'
            }),
        }
class EarningForm(forms.ModelForm):
    class Meta:
        model = Earning
        fields = ['earning_amount']
        widgets = {
            'earning_amount': forms.NumberInput(attrs={
                'id': 'earning-amount',
                'placeholder': 'Enter Cost of Product'
            }),
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['total_amount']

    total_amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'id': 'total-amount',
            'placeholder': 'Enter Total Amount'
        }),
        required=True
    )