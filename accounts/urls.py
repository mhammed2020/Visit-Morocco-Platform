from django.urls import path
from .views import (
    DestinationListView,
   
    
)
from . import views

urlpatterns = [
    # path('', views.home, name='home')
    path('', DestinationListView.as_view(), name='home'),

]
