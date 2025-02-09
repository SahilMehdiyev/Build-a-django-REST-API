import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name = 'price',
        lookup_expr='gte'
    )
    max_price = django_filters.NumberFilter(
        field_name = 'price',
        lookup_expr='lte'
    )
    title = django_filters.CharFilter(
        field_name = 'title',
        lookup_expr='icontains'
    )
    content = django_filters.CharFilter(
        field_name = 'content',
        lookup_expr='icontains'
    )
    public = django_filters.BooleanFilter(
        field_name = 'public'
    )
    owner = django_filters.NumberFilter(
        field_name='user',
        lookup_expr='exact'
    )
    
    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'title', 'content', 'public', 'owner']