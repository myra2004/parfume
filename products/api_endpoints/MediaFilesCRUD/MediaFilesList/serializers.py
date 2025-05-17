from rest_framework import serializers

from common.models import MediaFile


class MediaFileGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'