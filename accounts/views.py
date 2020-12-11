from django.shortcuts import render,get_object_or_404

from django.views.generic import (
    ListView,
    CreateView,
  
)
from . models import Destination
# Create your views here.
# def home(request) :
    
#     destinations = Destination.objects.all()


#     context = {
#         'destinations' :destinations
#     }

#     return render(request,'accounts/home.html', context)

class DestinationListView(ListView):
    model = Destination
    template_name = 'accounts/home.html'  
    context_object_name = 'destinations'
    paginate_by = 2

class DestinationCreateView(CreateView):
    model = Destination
    fields = ['name','desc','price',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)