import os
import uuid

from PIL import Image
from django.db import models
from django.conf import settings
from django.utils import formats

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

def create_thumbnail(input_image, thumbnail_size=(256, 256)):
    if not input_image or input_image == "":
        return
    image = Image.open(input_image)
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)
    filename = scramble_uploaded_filename(None, os.path.basename(input_image.name))
    arrdata = filename.split(".")
    extension = arrdata.pop()
    basename = "".join(arrdata)
    new_filename = basename + "_thumb." + extension
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename

class UploadImage(models.Model):
    userId = models.IntegerField(default=1, unique=True)
    name = models.CharField(default="Name", max_length=200)
    thumbnail = models.ImageField("Thumbnail of uploaded image", blank=True)
    desc = models.TextField(default="description of image")
    image = models.ImageField(default="uploaded image")
    created_at = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.userId

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(UploadImage, self).save(force_update=force_update)

