from rest_framework import serializers
from .models import RomImageFile, MachineInfo
from users.models import UserProfile
from project.models import Project
from users.serializers import UserOptionListSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    member = UserOptionListSerializer(many=True, read_only=True)

    def __str__(self):
        return self.url

    class Meta:
        model = Project
        fields = ('id', 'name', 'member', 'svn', 'build', 'add_time')


class ProjectCreateSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.name

    class Meta:
        model = Project
        fields = ('name', 'member', 'svn', 'build')


class ProjectNameSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.url

    class Meta:
        model = Project
        fields = ('id', 'name')


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
        if obj.project is None:
            return "未分配"
        return obj.user.username

    def get_create_time(self, obj):
        return obj.add_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_project(self, obj):
        if obj.project is None:
            return "未分配"

        return obj.project.name

    def get_project_id(self, obj):
        if obj.project is None:
            return None

        return obj.project.id

    def __str__(self):
        return self.url

    class Meta:
        model = RomImageFile
        fields = ('id', 'url', 'release_note', 'release_note_name', 'user', 'name',
                  'username', 'create_time', 'project', 'project_id', 'description')


class RomImageFilePatchSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.id

    class Meta:
        model = RomImageFile
        fields = ('id', 'project', 'description')


class RomImageFileCreateSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.name

    class Meta:
        model = RomImageFile
        fields = ('name', 'user', 'project', 'description', 'release_note', 'target_mails')


class RomImageFileListSerializer(serializers.Serializer):
    # roms = serializers.ListField(
    #     child=serializers.FileField(max_length=100000,
    #                                 allow_empty_file=False,
    #                                 use_url=True),
    #     write_only=True
    # )
    # description = serializers.CharField(max_length=None, min_length=5, allow_blank=False, trim_whitespace=True),
    roms = serializers.FileField(max_length=100000,
                                 allow_empty_file=False,
                                 use_url=True,
                                 write_only=True)

    release_note = serializers.FileField(max_length=100000,
                                         allow_empty_file=False,
                                         use_url=True,
                                         write_only=True)

    def create(self, validated_data):
        roms = validated_data.get('roms')
        release_note = validated_data.get('release_note')
        # self.context['request'].data["release_note"]
        project = self.context['request'].data["project"]
        description = self.context['request'].data["description"]

        images = []
        # for index, url in enumerate(roms):
        rom_file = RomImageFile.objects.create(
            name=roms.name,
            url=roms,
            release_note=release_note,
            release_note_name=release_note.name,
            user=UserProfile.objects.get(id=self.context['request'].user.id),
            project=Project.objects.get(id=project),
            description=description,
        )
        blog = RomImageFileSerializer(rom_file, context=self.context)
        # TODO 正确返回响应数据
        images.append(blog.data.serializer.data)
        print(images)
        return images


class MachineInfoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), help_text="所有者 ID")
    username = serializers.SerializerMethodField(help_text="所有者")
    userid = serializers.SerializerMethodField(help_text="所有者 ID")
    project = serializers.SerializerMethodField(help_text="所属项目")
    project_id = serializers.SerializerMethodField(help_text="所属项目 ID")
    create_time = serializers.SerializerMethodField(help_text="机器记录创建时间")
    start_time = serializers.SerializerMethodField(help_text="机器使用起始时间")
    end_time = serializers.SerializerMethodField(help_text="机器使用结束时间")

    def get_userid(self, obj):

        return obj.user.id

    def get_username(self, obj):

        return obj.user.username

    def get_create_time(self, obj):
        return obj.add_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_start_time(self, obj):
        if obj.start_time is None:
            return None
        else:
            return obj.start_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_end_time(self, obj):
        if obj.end_time is None:
            return None
        else:
            return obj.end_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_project(self, obj):
        return obj.project.name

    def get_project_id(self, obj):
        return obj.project.id

    def __str__(self):
        return self.url

    class Meta:
        model = MachineInfo
        fields = ('id',
                  'BMC_ip',
                  'Host_ip',
                  'user',
                  'web_username',
                  'web_password',
                  'username',
                  'userid',
                  'create_time',
                  'project',
                  'project_id',
                  'description',
                  'current_state',
                  'start_time',
                  'end_time'
                  )


class CreateMachineSerializer(serializers.ModelSerializer):
    def __str__(self):
        return self.BMC_ip

    # def validate_start_time(self, value):
    #     return value
    #
    # def validate_end_time(self, value):
    #     return value

    class Meta:
        model = MachineInfo
        fields = ('id',
                  'BMC_ip',
                  'Host_ip',
                  'web_username',
                  'web_password',
                  'description',
                  'project',
                  'user',
                  'current_state',
                  'start_time',
                  'end_time'
                  )
        # extra_kwargs = {
        #     'start_time': {'required': False},
        #     'end_time': {'required': False}
        # }

    def validate_start_time(self, value):
        # if 'django' not in value.lower():
        #     raise serializers.ValidationError("图书不是关于Django的")
        return value

    def validate_end_time(self, value):
        # if 'django' not in value.lower():
        #     raise serializers.ValidationError("图书不是关于Django的")
        return value

