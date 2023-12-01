from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def home(request):
    context = {"tasks": Task.objects.all()}
    return render(request, "todo/home.html", context)
