from django import forms
from .models import Customer

#create a class to represent what you want to do
class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
