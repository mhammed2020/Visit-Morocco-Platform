from django.urls import path
from .views import (
    DestinationListView,
    DestinationCreateView,
    DestinationUpdateView,
    DestinationDeleteView,
    
   
    
)
from . import views


from django.conf.urls import url
from django_filters.views import FilterView
from . filters import DestinationFilter


urlpatterns = [
    path('', views.home, name='home'),
    path('', DestinationListView.as_view(), name='home'),

    path('search/', FilterView.as_view(filterset_class=DestinationFilter,
        template_name='accounts/home.html'), name='search'),

    path('post/new/', DestinationCreateView.as_view(), name='post-create'),
    path('detail/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/update/', DestinationUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DestinationDeleteView.as_view(), name='post-delete'),


   path('about/', views.about, name='about')


]
