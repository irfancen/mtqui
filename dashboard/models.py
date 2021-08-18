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
    kapasitas_kelompok = models.IntegerField(null=True, blank=True)
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
    
    def get_tipe(self):
        return str(self.tipe)

    def can_enroll(self):
        is_before_deadline = not self.is_deadline()
        quota_available = self.get_enrollment_count() < self.kuota
        return (is_before_deadline and quota_available)
    
    def can_view_enrollments(self):
        has_enrollment = self.get_enrollment_count() > 0
        return has_enrollment

    def __str__(self):
        return f"{self.judul} ({self.fakultas.metadata.nama_fakultas})"


class Kelompok(models.Model):
    nama = models.CharField(max_length=100)
    kompetisi = models.ForeignKey(Kompetisi, on_delete=models.CASCADE, related_name="kelompok")

    def get_kapasitas(self):
        return self.kompetisi.kapasitas_kelompok
    
    def get_ketua(self):
        for anggota in self.anggota.all():
            if anggota.is_ketua:
                return anggota
        return None
    
    def get_ketua_choices(self):
        return ( (anggota.id, anggota.nama) for anggota in self.anggota.all() )
    
    def get_tipe(self):
        return self.kompetisi.get_tipe()

    def can_add_member(self):
        is_before_deadline = not self.kompetisi.is_deadline()
        capacity_available = self.anggota.all().count() < self.kompetisi.kapasitas_kelompok
        return (is_before_deadline and capacity_available)
    
    def can_be_edited(self):
        is_before_deadline = not self.kompetisi.is_deadline()
        return is_before_deadline

    def can_be_deleted(self):
        is_before_deadline = not self.kompetisi.is_deadline()
        return is_before_deadline
    
    def __str__(self):
        return self.nama


class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=50)
    angkatan = models.CharField(max_length=4)
    no_hp = models.CharField(max_length=15)
    line_id = models.CharField(max_length=30)
    is_ketua = models.BooleanField(null=True, blank=True) # Only for DAQ

    foto_ktm = models.ImageField()
    screenshot_siak = models.ImageField()
    file_cv = models.FileField(null=True, blank=True) # Only for DAQ

    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE, related_name="anggota")

    def get_tipe(self):
        return self.kelompok.get_tipe()

    def can_be_edited(self):
        is_before_deadline = not self.kelompok.kompetisi.is_deadline()
        return is_before_deadline

    def can_be_deleted(self):
        is_before_deadline = not self.kelompok.kompetisi.is_deadline()
        will_still_have_members = (self.kelompok.anggota.all().count() - 1) > 0
        return (is_before_deadline and will_still_have_members)

    def __str__(self):
        return self.nama


class Peserta(models.Model):
    nama = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=50)
    angkatan = models.CharField(max_length=4)
    no_hp = models.CharField(max_length=15)
    line_id = models.CharField(max_length=30)

    foto_ktm = models.ImageField()
    screenshot_siak = models.ImageField()

    kompetisi = models.ForeignKey(Kompetisi, on_delete=models.CASCADE, related_name="peserta")

    def can_be_edited(self):
        is_before_deadline = not self.kompetisi.is_deadline()
        return is_before_deadline

    def can_be_deleted(self):
        is_before_deadline = not self.kompetisi.is_deadline()
        return is_before_deadline

    def __str__(self):
        return self.nama
