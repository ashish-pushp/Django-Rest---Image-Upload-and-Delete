from rest_framework import viewsets, filters
from imageupload_rest.serializers import UploadedImageSerializer
from imageupload.models import UploadImage

class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadedImageSerializer


    def delete(self, *args, **kwargs):
        pass