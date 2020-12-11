from django.shortcuts import render,get_object_or_404
from . models import Destination
# Create your views here.
def home(request) :
    
    destinations = Destination.objects.all()


    context = {
        'destinations' :destinations
    }

    return render(request,'accounts/home.html', context)