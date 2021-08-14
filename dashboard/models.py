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


class TipeKompetisi(models.Model):
    tipe = models.CharField(max_length=20)

    def __str__(self):
        return self.tipe


class Kompetisi(models.Model):
    judul = models.CharField(max_length=100)
    kuota = models.IntegerField()
    deadline_pendaftaran = models.DateField()
    tipe = models.ForeignKey(TipeKompetisi, on_delete=models.SET_NULL, related_name="kompetisi", null=True)
    fakultas = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kompetisi")

    def get_enrollment_count(self):
        if str(self.tipe) == "Individu":
            return self.peserta.all().count()
        else:
            return self.kelompok.all().count()        

    def get_deadline(self):
        return self.deadline_pendaftaran.strftime("%d - %b - %Y")
    
    def is_deadline(self):
        return datetime.now(timezone(settings.TIME_ZONE)).date() > self.deadline_pendaftaran

    def can_enroll(self):
        is_before_deadline = not self.is_deadline()
        quota_available = self.get_enrollment_count() < self.kuota
        return (is_before_deadline and quota_available)
    
    def can_edit_enrollments(self):
        is_before_deadline = not self.is_deadline()
        has_enrollment = self.get_enrollment_count() > 0
        return (is_before_deadline and has_enrollment)
    
    def can_view_enrollments(self):
        is_after_deadline = self.is_deadline()
        has_enrollment = self.get_enrollment_count() > 0
        return (is_after_deadline and has_enrollment)

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
