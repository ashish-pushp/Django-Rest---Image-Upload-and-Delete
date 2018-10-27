from rest_framework import serializers
from imageupload.models import UploadImage

class UploadedImageSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    class Meta:
        model = UploadImage
        fields = ('pk','userId', 'name','thumbnail', 'desc', 'image', 'created_at')
        read_only_fields = ('thumbnail','created_at')