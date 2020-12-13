import django_filters
from .models import Destination
class DestinationFilter(django_filters.FilterSet):

    desc = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Destination
        fields = '__all__'
        exclude = ['img','price','offer','author','date_posted']
