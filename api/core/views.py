from django.shortcuts import render
from django.http import JsonResponse


def ping_pong(request):
    return JsonResponse('Pong!', safe=False)