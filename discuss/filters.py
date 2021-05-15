import django_filters
from django_filters import CharFilter

from .models import *


class DiscussFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Discussion
        fields = '__all__'
        exclude = ['creation_time', 'updated', 'content', 'author', 'discussion_picture']
