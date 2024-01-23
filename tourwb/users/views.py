from django.http import HttpResponse

def basket(request):
    return HttpResponse('Корзина')

def personal_account(request):
    return HttpResponse('Личный кабинет')

def payment(request):
    return HttpResponse(f'Страница оплаты')