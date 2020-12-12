from django.shortcuts import render,get_object_or_404

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
  
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
    paginate_by = 4

class DestinationCreateView(CreateView):
    model = Destination
    fields = ['name','img','desc','price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def post_detail(request,post_id) :
    
    post = get_object_or_404(Destination,pk=post_id)
   
    context ={
        'title':post,
        'post' : post,
    }


   
    return render(request,'accounts/post_detail.html', context)

class DestinationUpdateView(UpdateView):
    model = Destination
    fields = ['name','img','desc','price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Destination
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False