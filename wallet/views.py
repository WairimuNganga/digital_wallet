from django.shortcuts import render
from .forms import CustomerRegistrationForm

# Create your views here.
#Contents of a HTTP request
def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

#Routes-They determine which function is to be followed