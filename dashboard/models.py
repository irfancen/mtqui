from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class MetadataFakultas(models.Model):
    fakultas = models.OneToOneField(User, on_delete=models.CASCADE, related_name="metadata")
    nama_fakultas = models.CharField(max_length=50)
    singkatan_fakultas = models.CharField(max_length=20)
    makara_image_code = models.CharField(max_length=20)
