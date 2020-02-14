from rest_framework import serializers
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
from django.http.response import JsonResponse

from .models import RomImageFile,MachineInfo
from users.serializers import UserSerializer
from users.models import UserProfile
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    member = serializers.SlugRelatedField(many=True,read_only=True,slug_field='username')

    def __str__(self):
        return self.url

    class Meta:
        model = Project
        fields = ('id', 'name','member','svn','build','add_time')


class ProjectCreateSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.name

    class Meta:
        model = Project
        fields = ('name','member','svn','build')


class ProjectNameSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.url

    class Meta:
        model = Project
        fields = ('id','name')


class RomImageFileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()

    project_id = serializers.SerializerMethodField()

    create_time = serializers.SerializerMethodField()

    def create(self, validated_data):
        user = self.context["request"].user
        return RomImageFile.objects.create(**validated_data)

    def get_username(self, obj):
       return obj.user.username

    def get_create_time(self,obj):
        return obj.add_time.strftime('%Y-%m-%d %I:%M:%S')

    def get_project(self, obj):
       return obj.project.name

    def get_project_id(self, obj):
       return obj.project.id

    def __str__(self):
        return self.url

    class Meta:
        model = RomImageFile
        fields = ('id', 'url', 'user', 'name','username', 'create_time', 'project','project_id','description')


class RomImageFilePatchSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.id

    class Meta:
        model = RomImageFile
        fields = ('id', 'project','description')


class RomImageFileListSerializer(serializers.Serializer):
    roms = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=True),write_only=True
    )
    rom_files = serializers.ListField(
        child=serializers.CharField(max_length=1000,),read_only=True
    )

    def create(self, validated_data):
        roms = validated_data.get('roms')
        project = self.context['request'].data["project"]
        description = self.context['request'].data["description"]

        images = []
        for index, url in enumerate(roms):
            rom_file = RomImageFile.objects.create(name=url.name, url=url,
                                                   user= UserProfile.objects.get(id=self.context['request'].user.id),
                                                   project=Project.objects.get(id=project),
                                                   description=description,

                                                   )
            blog = RomImageFileSerializer(rom_file, context=self.context)
            # TODO 正确返回响应数据
            images.append(blog.data.serializer.data)
            print(images)
        return images

class MachineInfoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(),help_text="所有者 ID")
    username = serializers.SerializerMethodField(help_text="所有者")
    project = serializers.SerializerMethodField(help_text="所属项目")
    project_id = serializers.SerializerMethodField(help_text="所属项目 ID")
    create_time = serializers.SerializerMethodField(help_text="机器记录创建时间")

    def get_username(self, obj):
       return obj.user.username

    def get_create_time(self,obj):
        return obj.add_time.strftime('%Y-%m-%d %I:%M:%S')

    def get_project(self, obj):
       return obj.project.name

    def get_project_id(self, obj):
       return obj.project.id

    def __str__(self):
        return self.url

    class Meta:
        model = MachineInfo
        fields = ('id', 'BMC_ip','Host_ip', 'user','web_username','web_password', 'username', 'create_time', 'project', 'project_id', 'description')


class CreateMachineSerializer(serializers.ModelSerializer):
    def __str__(self):
        return self.BMC_ip

    class Meta:
        model = MachineInfo
        fields = ('id','BMC_ip','Host_ip','web_username','web_password','description','project','user')




