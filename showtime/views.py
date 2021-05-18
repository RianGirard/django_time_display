from django.shortcuts import render
from time import gmtime, strftime, strptime
import datetime

def index(request):
    return render(request, "index.html")

def showtime(request):
    context = {
        # "time": strftime("%b %d, %Y  %H:%M %p", gmtime())     # First method that returns UTC time 
        "time": datetime.datetime.now()                         # Second method that returns local time
    }
    return render(request, "showtime.html", context)

# Create your views here.
