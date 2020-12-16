from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
  
)
from . models import Destination
from . forms import DestinationForm

from .filters import DestinationFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth.models import User  # ----------------------------Tracking User

# Create your views here.
# function based view 

def home(request) :
    
    destinations = Destination.objects.all()
   

    myfilter = DestinationFilter(request.GET, queryset=destinations)
    destinations = myfilter.qs
    """paginator must be after  django filter."""

    paginator = Paginator(destinations,4)
    page = request.GET.get('page')

    try:
  
        destinations = paginator.page(page)
        

       
    except PageNotAnInteger:
        destinations = paginator.page(1)
    except EmptyPage:
        destinations = paginator.page(paginator.num_page)

    

    
    # paginator = Paginator(destinations, 4)  # Show 25 contacts per page.
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)


    context = {
        'destinations' :destinations,
        'myfilter': myfilter,
         'page':page
    }

    return render(request,'accounts/home.html', context)







class DestinationListView(ListView):
    model = Destination
    template_name = 'accounts/home.html'  
    context_object_name = 'destinations'
    paginate_by = 4

    # def get_queryset(self):
    #     qs = self.model.objects.all()
    #     myfilter = DestinationFilter(self.request.GET, queryset=qs)
    #     return myfilter.qs
     




class DestinationCreateView(LoginRequiredMixin,CreateView):
    model = Destination
    # form_class = DestinationForm 
    fields = ['name','img','desc','price']
    # template_name = 'accounts/destination_form.html'
    # success_url = '/'
        
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



class DestinationUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
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


class DestinationDeleteView(DeleteView):
    model = Destination
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'accounts/about.html', {'title': 'About'})




def dashboard(request):
    

    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})







    # tracking user 

def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,'account/user/list.html',{'section': 'people','users': users})


def user_detail(request, username):
    pass
    