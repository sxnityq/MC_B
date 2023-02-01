from collections import OrderedDict
from collections.abc import Mapping

from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import get_error_detail, set_value, SkipField
from rest_framework.exceptions import ValidationError
from rest_framework.settings import api_settings


from .models import NewsItem, CustomUser, Album

class NewsSerializer(ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = ("title", "slug", "descr", "image", "creation_date")


class CustomUserSerializer(serializers.Serializer):
    
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    email = serializers.EmailField(max_length=64, required=True)
    username = serializers.CharField(max_length=32, required=True)

    def validate(self, attrs):
        if attrs.get('password1') != attrs.get('password2'):
            raise serializers.ValidationError({'password1':'passwords do not match',
                                                'password2':'passwords do not match'})
        return attrs
    
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
        if data.get('password1') != data.get('password2'):
            errors['password1'] = ['passwords do not match']
            errors['password2'] = ['passwords do not match']
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
    
    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        validated_data['password'] = password
        return CustomUser.objects.create(**validated_data)
        

        

class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = ("title", "slug", "description")    