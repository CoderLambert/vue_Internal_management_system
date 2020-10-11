from rest_framework import serializers
from support.models import WebSiteLink, WebSiteType, ResourceType, CloundResource, Demand


class WebSiteLinkSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    typeid = serializers.SerializerMethodField()

    # owner = serializers.SerializerMethodField()

    def get_type(self, obj):
        if obj.type is None:
            return "未分配"
        return obj.type.name

    def get_typeid(self, obj):
        if obj.type is None:
            return "未分配"
        return obj.type.id
    # def get_owner(self, obj):
    #     if obj.owner is None:
    #         return "未分配"
    #     return obj.owner.username

    def __str__(self):
        return self.name

    class Meta:
        model = WebSiteLink
        fields = ('id', 'name', 'public', 'url', 'description', 'type', 'typeid')


class WebSiteLinkCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.name

    class Meta:
        model = WebSiteLink
        fields = ('name', 'url', 'description', 'public', 'type', 'owner',)


class WebSiteTypeSerializer(serializers.ModelSerializer):
    # owner = serializers.SerializerMethodField()
    #
    # def get_owner(self, obj):
    #     if obj.owner is None:
    #         return "未分配"
    #     return obj.owner.username

    def __str__(self):
        return self.name

    class Meta:
        model = WebSiteType
        fields = ('id', 'name',  'order',)  # 'owner',


class WebSiteTypeCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.name

    class Meta:
        model = WebSiteType
        fields = ('name',  'order',  'owner')

class ResourceTypeSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    def get_owner(self, obj):
        if obj.owner is None:
            return "未分配"
        return obj.owner.username

    def __str__(self):
        return self.name

    class Meta:
        model = ResourceType
        fields = ('id', 'name', 'owner',)


class ResourceTypeCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.name

    class Meta:
        model = ResourceType
        fields = ('name', 'owner',)


class DemandSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    def get_owner(self, obj):
        if obj.owner is None:
            return "未分配"
        return obj.owner.username

    def __str__(self):
        return self.name

    class Meta:
        model = Demand
        fields = ('id', 'description', 'owner', 'current_state', 'add_time',)


class DemandCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.description

    class Meta:
        model = Demand
        fields = ('description', 'owner',)


class CloundResourceSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    def get_owner(self, obj):
        if obj.owner is None:
            return "未分配"
        return obj.owner.username

    def __str__(self):
        return self.name

    class Meta:
        model = WebSiteType
        fields = ('id', 'name', 'owner',)


class CloundResourceCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.name

    class Meta:
        model = CloundResource
        fields = ('name', 'owner')
