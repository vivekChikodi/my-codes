from django.shortcuts import render
from django.http import HttpResponse

def search(request, bookmark_id):
    return HttpResponse("You're looking at bookmark %s." % bookmark_id)

def results(request, bookmark_id):
    response = "You're looking at the results of search %s."
    return HttpResponse(response % bookmark_id)

def add(request, bookmark_id):
    return HttpResponse("You're voting on question %s." % bookmark_id)

def index(request):
    return HttpResponse("Hello, world. You're at the todo index.")

# Create your views here.
