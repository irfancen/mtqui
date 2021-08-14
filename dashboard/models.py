from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from pytz import timezone

# Create your models here.
class MetadataFakultas(models.Model):
    username_fakultas = models.OneToOneField(User, on_delete=models.CASCADE, related_name="metadata")
    nama_fakultas = models.CharField(max_length=50)
    singkatan_fakultas = models.CharField(max_length=20)
    makara = models.ImageField(upload_to="makara/")

    def __str__(self):
        return self.nama_fakultas

class Kompetisi(models.Model):
    judul = models.CharField(max_length=100)
    kuota = models.IntegerField()
    deadline_pendaftaran = models.DateField()
    fakultas = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kompetisi")

    def get_ketua(self):
        result = None

        for peserta in self.peserta.all():
            if peserta.is_ketua:
                result = peserta
                break

        return result

    def get_deadline(self):
        return self.deadline_pendaftaran.strftime("%d - %b - %Y")
    
    def is_deadline(self):
        return datetime.now(timezone(settings.TIME_ZONE)).date() > self.deadline_pendaftaran

    def can_enroll(self):
        is_before_deadline = not self.is_deadline()
        no_participants = self.peserta.all().count() == 0

        return (is_before_deadline and no_participants)
    
    def can_edit_enrollments(self):
        is_before_deadline = not self.is_deadline()
        have_participants = self.peserta.all().count() > 0

        return (is_before_deadline and have_participants)
    
    def can_see_enrollments(self):
        is_after_deadline = self.is_deadline()
        have_participants = self.peserta.all().count() > 0

        return (is_after_deadline and have_participants)

    def __str__(self):
        return f"{self.judul} ({self.fakultas.metadata.nama_fakultas})"

class Peserta(models.Model):
    nama = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=50)
    angkatan = models.CharField(max_length=4)
    no_hp = models.CharField(max_length=15)
    line_id = models.CharField(max_length=30)
    foto_ktm = models.ImageField(upload_to="foto_ktm")
    screenshot_siak = models.ImageField(upload_to="screenshot_siak")
    file_cv = models.FileField(upload_to="file_cv")
    is_ketua = models.BooleanField()
    kompetisi = models.ForeignKey(Kompetisi, on_delete=models.CASCADE, related_name="peserta")

    def __str__(self):
        return f"{self.nama}"
