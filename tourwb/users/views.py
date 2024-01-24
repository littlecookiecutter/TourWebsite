from django.http import HttpResponse
from django.shortcuts import render

def basket(request):
    template = 'users/basket.html'
    return render(request, template)

def personal_account(request):
    template = 'users/personal_account.html'
    return render(request, template)

def payment(request):
    template = 'users/payment.html'
    return render(request, template)