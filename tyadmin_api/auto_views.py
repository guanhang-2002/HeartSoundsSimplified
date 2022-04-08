
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from User.models import Users
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from Exhibition.models import HeartSounds, Introduce, Dynamic, PopuOfScience

from tyadmin_api.auto_serializers import UsersListSerializer, PermissionListSerializer, GroupListSerializer, ContentTypeListSerializer, HeartSoundsListSerializer, IntroduceListSerializer, DynamicListSerializer, PopuOfScienceListSerializer
from tyadmin_api.auto_serializers import UsersCreateUpdateSerializer, PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, HeartSoundsCreateUpdateSerializer, IntroduceCreateUpdateSerializer, DynamicCreateUpdateSerializer, PopuOfScienceCreateUpdateSerializer
from tyadmin_api.auto_filters import UsersFilter, PermissionFilter, GroupFilter, ContentTypeFilter, HeartSoundsFilter, IntroduceFilter, DynamicFilter, PopuOfScienceFilter

    
class UsersViewSet(XadminViewSet):
    serializer_class = UsersListSerializer
    queryset = Users.objects.all().order_by('-pk')
    filter_class = UsersFilter
    search_fields = ["password","username","first_name","last_name","email","is_professional"]

    def get_serializer_class(self):
        if self.action == "list":
            return UsersListSerializer
        else:
            return UsersCreateUpdateSerializer

    
class PermissionViewSet(XadminViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all().order_by('-pk')
    filter_class = PermissionFilter
    search_fields = ["name","codename"]

    def get_serializer_class(self):
        if self.action == "list":
            return PermissionListSerializer
        else:
            return PermissionCreateUpdateSerializer

    
class GroupViewSet(XadminViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().order_by('-pk')
    filter_class = GroupFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GroupListSerializer
        else:
            return GroupCreateUpdateSerializer

    
class ContentTypeViewSet(XadminViewSet):
    serializer_class = ContentTypeListSerializer
    queryset = ContentType.objects.all().order_by('-pk')
    filter_class = ContentTypeFilter
    search_fields = ["app_label","model"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentTypeListSerializer
        else:
            return ContentTypeCreateUpdateSerializer

    
class HeartSoundsViewSet(XadminViewSet):
    serializer_class = HeartSoundsListSerializer
    queryset = HeartSounds.objects.all().order_by('-pk')
    filter_class = HeartSoundsFilter
    search_fields = ["name","file_path"]

    def get_serializer_class(self):
        if self.action == "list":
            return HeartSoundsListSerializer
        else:
            return HeartSoundsCreateUpdateSerializer

    
class IntroduceViewSet(XadminViewSet):
    serializer_class = IntroduceListSerializer
    queryset = Introduce.objects.all().order_by('-pk')
    filter_class = IntroduceFilter
    search_fields = ["name","sample_from","duration_for_sample","style_of_sampling","sample_frequency"]

    def get_serializer_class(self):
        if self.action == "list":
            return IntroduceListSerializer
        else:
            return IntroduceCreateUpdateSerializer

    
class DynamicViewSet(XadminViewSet):
    serializer_class = DynamicListSerializer
    queryset = Dynamic.objects.all().order_by('-pk')
    filter_class = DynamicFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return DynamicListSerializer
        else:
            return DynamicCreateUpdateSerializer

    
class PopuOfScienceViewSet(XadminViewSet):
    serializer_class = PopuOfScienceListSerializer
    queryset = PopuOfScience.objects.all().order_by('-pk')
    filter_class = PopuOfScienceFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return PopuOfScienceListSerializer
        else:
            return PopuOfScienceCreateUpdateSerializer
