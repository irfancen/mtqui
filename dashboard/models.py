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
    makara_image_code = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_fakultas

class Kompetisi(models.Model):
    judul = models.CharField(max_length=100)
    kuota = models.IntegerField()
    deadline_pendaftaran = models.DateField()
    fakultas = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kompetisi")

    def get_deadline(self):
        return self.deadline_pendaftaran.strftime("%d - %b - %Y")
    
    def is_deadline(self):
        return datetime.now(timezone(settings.TIME_ZONE)).date() > self.deadline_pendaftaran

    def can_enroll(self):
        is_before_deadline = not self.is_deadline()
        have_quota = self.peserta.all().count() < self.kuota

        return (is_before_deadline and have_quota)
    
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
    npm = models.CharField(max_length=10)
    kompetisi = models.ForeignKey(Kompetisi, on_delete=models.CASCADE, related_name="peserta")

    def __str__(self):
        return f"{self.npm} - {self.nama}"
