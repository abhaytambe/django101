from django.http import HttpResponse 
from django.shortcuts import render

def greeting(request):
    return HttpResponse("Hello, welcome to Django :<) ")


def translator(request):
    return render(request, 'translator.html')

def translatorOutput(request):
    return render(request, 'translatorOutput.html', {'input': "ABC", 'translatedData' : 'CBA - ABC' })

def aboutUs(request):
    return render (request, 'aboutUs.html')  