from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # now we must add bootsrtrap content
    return render(request, "todo/home.html")
