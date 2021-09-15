from django.shortcuts import render
from .models import Event
# Create your views here.
def showevens(request):
    evets = Event.objects
    return render(request, 'events/home.html', {'evens': evets})
