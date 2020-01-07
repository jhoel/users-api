from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    full_name = CharField(source='get_full_name', read_only=True)
    absolute_url = CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'full_name',
                  'email', 'phone', 'image_profile', 'absolute_url']
