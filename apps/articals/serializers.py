from rest_framework import serializers
from articals.models import Articale, Note, ImageMeta, ArticleType
from django.contrib.auth import get_user_model

User = get_user_model()


class NoteSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    def __str__(self):
        return self.name

    def get_articles(self, obj):
        return obj.articles.count()

    class Meta:
        model = Note
        fields = ('id', 'name', 'add_time', 'modified_time', 'articles')


class NoteCreateSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.name

    class Meta:
        model = Note
        fields = ('name',)


class ArticleTypeSerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()

    def get_parent_name(self, obj):
        if obj.parent is not None:
            return obj.parent.name
        else:
            return None

    def get_articles(self, obj):
        return obj.articles.filter(public=True).count()

    def __str__(self):
        return self.name

    class Meta:
        model = ArticleType
        fields = ('id', 'name', 'parent', 'parent_name', 'add_time', 'modified_time', 'articles')


class ArticleTypeCreateSerializer(serializers.ModelSerializer):
    def __str__(self):
        return self.name

    class Meta:
        model = ArticleType
        fields = ('name', 'parent')


class ArticaleSerializer(serializers.ModelSerializer):
    note = serializers.SerializerMethodField()
    add_time = serializers.SerializerMethodField()
    modified_time = serializers.SerializerMethodField()
    user_info = serializers.SerializerMethodField()
    types = ArticleTypeSerializer(many=True, read_only=True)

    def get_note(self, obj):
        return {'name': obj.note.name,
                'id': obj.note.id
                }

    def get_add_time(self, obj):
        return obj.add_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_modified_time(self, obj):
        return obj.modified_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_user_info(self, obj):
        return {'name': obj.user.username,
                'id': obj.user.id
                }

    def __str__(self):
        return self.title

    class Meta:
        model = Articale
        fields = (
            'id', 'note', 'title', 'original', 'orginal_link', 'public', 'user_info', 'browse_num',
            'add_time', 'modified_time', 'types')


class ArticaleDetailSerializer(serializers.ModelSerializer):
    note = serializers.SerializerMethodField()
    add_time = serializers.SerializerMethodField()
    modified_time = serializers.SerializerMethodField()
    user_info = serializers.SerializerMethodField()
    types = ArticleTypeSerializer(many=True, read_only=True)

    def get_note(self, obj):
        return {'name': obj.note.name,
                'id': obj.note.id
                }

    def get_add_time(self, obj):
        return obj.add_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_modified_time(self, obj):
        return obj.modified_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_user_info(self, obj):
        return {'name': obj.user.username,
                'id': obj.user.id
                }

    def get_types(self, obj):
        return {
            'id': obj.types.id,
            'name': obj.types.name
        }

    def __str__(self):
        return self.title

    class Meta:
        model = Articale
        fields = (
            'id', 'note', 'title', 'text_content', 'original', 'orginal_link', 'public', 'user_info', 'browse_num',
            'add_time', 'modified_time', 'types')


class ArticaleCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.title

    class Meta:
        model = Articale
        fields = ('id', 'note', 'title', 'text_content', 'original', 'orginal_link', 'public', 'user', 'types')


class ImageFileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_name = serializers.SerializerMethodField()

    def create(self, validated_data):
        user = self.context["request"].user
        return ImageMeta.objects.create(**validated_data)

    def get_user_name(self, obj):
        if obj.user is None:
            return "未分配"
        return obj.user.user_name

    def __str__(self):
        return self.Image.name

    class Meta:
        model = ImageMeta
        fields = ('id', 'image', 'user_name')


class ImageFileSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        if obj.user is None:
            return "未分配"
        return obj.user.user_name

    def __str__(self):
        return self.Image.name

    class Meta:
        model = ImageMeta
        fields = ('id', 'image', 'user_name')


class ImageFileCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.image

    class Meta:
        model = ImageMeta
        fields = ('id', 'image', 'user')
