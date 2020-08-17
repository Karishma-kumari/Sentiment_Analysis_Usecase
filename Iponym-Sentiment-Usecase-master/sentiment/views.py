from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .Controller import entry_point

# Create your views here.


def model_metrics(request):
    response = entry_point.get_model_metrics()
    return JsonResponse(response)


def sentiment(request):
    response = entry_point.getting_sentiment()
    return JsonResponse(response)

def reviews(request):
    response = entry_point.display_reviews()
    return HttpResponse(response)