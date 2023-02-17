from collections import OrderedDict
from collections.abc import Mapping

from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import get_user_model, password_validation

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import get_error_detail, set_value, SkipField
from rest_framework.exceptions import ValidationError
from rest_framework.settings import api_settings

from .models import NewsItem, CustomUser, Album, AlbumElement
from .utils import str_to_int


User = get_user_model()

class NewsSerializer(ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = ("title", "slug", "descr", "image", "creation_date")


class CustomUserSerializer(serializers.Serializer):
    
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=64, required=True)
    username = serializers.CharField(max_length=32, required=True)

    def validate_email(self, value):
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(detail="email already exists")
        return value

    def validate_username(self, value):
        
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(detail="username already exists")
        return value
    
    def to_internal_value(self, data):
        """
        Dict of native values <- Dict of primitive datatypes.
        """
        if not isinstance(data, Mapping):
            message = self.error_messages['invalid'].format(
                datatype=type(data).__name__
            )
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='invalid')
        ret = OrderedDict()
        errors = OrderedDict()
        
        password1_errors = []
        password2_errors = []
        if data.get('password1') != data.get('password2'):
            password1_errors.append('Passwords do not match')
            password2_errors.append('Passwords do not match')
        try:
            password_validation.validate_password(data.get('password1'))
        except DjangoValidationError as ex:
                password1_errors.extend(ex)
        try:
            password_validation.validate_password(data.get('password2'))
        except DjangoValidationError as ex:
                password2_errors.extend(ex)   
        
        errors["password1"] = password1_errors
        errors["password2"] = password2_errors
        
        fields = self._writable_fields

        for field in fields:
            validate_method = getattr(self, 'validate_' + field.field_name, None)
            primitive_value = field.get_value(data)
            try:
                validated_value = field.run_validation(primitive_value)
                if validate_method is not None:
                    validated_value = validate_method(validated_value)
            except ValidationError as exc:
                errors[field.field_name] = exc.detail
            except DjangoValidationError as exc:
                errors[field.field_name] = get_error_detail(exc)
            except SkipField:
                pass
            else:
                set_value(ret, field.source_attrs, validated_value)

        if errors:
            raise ValidationError(errors)

        return ret
    
    def save(self, **kwargs):
        password = self.validated_data.pop('password1')
        self.validated_data.pop('password2')
        self.validated_data['password'] = password
        return super().save(**kwargs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AlbumElementSerilaizer(serializers.ModelSerializer):
    
    class Meta:
        model = AlbumElement
        fields = ("image", "album")


class AlbumSerializer(serializers.ModelSerializer):
    
    images = serializers.SerializerMethodField()
    
    def get_images(self, obj):
        
        limit = self.context['request'].query_params.get('amount', '9')
        limit = str_to_int(limit)        
        query = AlbumElement.objects.select_related('album').filter(album=obj).all()[:limit]
        serializer = AlbumElementSerilaizer(query, many=True)
        return serializer.data
    
    class Meta:
        model = Album
        fields = ("title", "slug", "description", "images")


class AlbumElementSlugSerilaizer(serializers.ModelSerializer):
    
    images = serializers.SerializerMethodField()
    
    def get_images(self, obj):
        
        query = AlbumElement.objects.select_related('album').filter(album=obj).all()
        serializer = AlbumElementSerilaizer(query, many=True)
        return serializer.data    
    
    class Meta:
        model = Album
        fields = ("title", "slug", "description", "images")