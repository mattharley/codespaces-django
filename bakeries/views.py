from django.shortcuts import render

from .models import Bakery

def index(request):
    context = {
        "title": "Django example",
        "bakeries": Bakery.objects.all()
    }
    return render(request, "index.html", context)
