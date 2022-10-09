from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def View(request):
    json = {"Message": "Hello World!"}
    return JsonResponse(json)