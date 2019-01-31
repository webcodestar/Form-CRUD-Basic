from .models import Client
import django_filters


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['client_name', 'email', 'phone', 'suburb', ]
