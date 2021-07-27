from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class MetadataFakultas(models.Model):
    username_fakultas = models.OneToOneField(User, on_delete=models.CASCADE, related_name="metadata")
    nama_fakultas = models.CharField(max_length=50)
    singkatan_fakultas = models.CharField(max_length=20)
    makara_image_code = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_fakultas

class Peserta(models.Model):
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=10)

    class Meta:
        unique_together = ("nama", "npm")

    def __str__(self):
        return f"{self.npm} - {self.nama}"

class Kompetisi(models.Model):
    judul = models.CharField(max_length=100)
    kuota = models.IntegerField()
    deadline_pendaftaran = models.DateField()
    fakultas = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kompetisi")
    peserta = models.ManyToManyField(Peserta, blank=True, related_name="kompetisi")

    def __str__(self):
        return f"{self.judul} ({self.fakultas.metadata.nama_fakultas})"
