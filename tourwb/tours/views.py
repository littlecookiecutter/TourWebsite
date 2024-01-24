from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'tours/index.html'
    return render(request, template)

def tours_list(request):
    template = 'tours/tours_list.html'
    return render(request, template)

def tours_detail(request, pk):
    template = 'tours/tours_detail.html'
    return render(request, pk, template)