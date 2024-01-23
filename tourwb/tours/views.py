from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def tours_list(request):
    return HttpResponse('Список туров')

def tours_detail(request, pk):
    return HttpResponse(f'Тур с названием {pk}')