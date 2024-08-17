import django_filters
from ..models import Author

class AuthorFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='iexact')
    birth_date = django_filters.DateFilter()
    birth_date_range = django_filters.DateFromToRangeFilter(field_name='birth_date')

    class Meta:
        model = Author
        fields = ['first_name', 'email', 'birth_date']