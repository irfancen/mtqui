from django.db import models


class Kegiatan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery", blank=True)

    def __str__(self):
        return self.image.name
