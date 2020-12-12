import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class DestinationFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')


    class Meta:
		model = Destination
		fields = '__all__'
