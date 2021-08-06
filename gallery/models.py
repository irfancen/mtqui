from django.db import models

class Kegiatan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    name = models.CharField(max_length=255)
    kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name