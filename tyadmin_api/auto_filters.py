from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from User.models import Users
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from Exhibition.models import HeartSounds, Introduce, Dynamic, PopuOfScience

class UsersFilter(filters.FilterSet):
    last_login = DateFromToRangeFilter(field_name="last_login")
    date_joined = DateFromToRangeFilter(field_name="date_joined")

    class Meta:
        model = Users
        exclude = ["photo","photo"]

class PermissionFilter(filters.FilterSet):
    content_type_text = filters.CharFilter(field_name="content_type")

    class Meta:
        model = Permission
        exclude = []

class GroupFilter(filters.FilterSet):

    class Meta:
        model = Group
        exclude = []

class ContentTypeFilter(filters.FilterSet):

    class Meta:
        model = ContentType
        exclude = []

class HeartSoundsFilter(filters.FilterSet):
    owner_text = filters.CharFilter(field_name="owner")
    created_time = DateFromToRangeFilter(field_name="created_time")

    class Meta:
        model = HeartSounds
        exclude = []

class IntroduceFilter(filters.FilterSet):
    heartSounds_text = filters.CharFilter(field_name="heartSounds")

    class Meta:
        model = Introduce
        exclude = []

class DynamicFilter(filters.FilterSet):
    heartSounds_text = filters.CharFilter(field_name="heartSounds")

    class Meta:
        model = Dynamic
        exclude = ["dynamicPicture","dynamicPicture"]

class PopuOfScienceFilter(filters.FilterSet):
    heartSounds_text = filters.CharFilter(field_name="heartSounds")

    class Meta:
        model = PopuOfScience
        exclude = []