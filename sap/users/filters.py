import django_filters

from users.models import *


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = User
        exclude = ['proImage', 'birthdate', 'wPhone','pPhone']