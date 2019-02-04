from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello guys, I am learning Django.</h1>")

# Anirudh Kumar- 7428232774