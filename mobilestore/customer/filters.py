import django_filters
from owner.models import Mobiles


class MobileFormSearch(django_filters.FilterSet):
    class Meta:
        model = Mobiles
        fields = ['mobile_name', 'price', 'model']
