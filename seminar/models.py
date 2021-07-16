from django.db import models

# Create your models here.
class GuestStars(models.Model):
    nama = models.CharField(max_length=150)

    def __str__(self):
        return self.nama

class Seminar(models.Model):
    judul_seminar = models.CharField(max_length=200)
    about = models.CharField(max_length=300)
    guest_stars = models.ManyToManyField(GuestStars)
    received = models.CharField(max_length=500)
    requirement = models.CharField(max_length=500)

    def __str__(self):
        return self.judul_seminar


class EventDate(models.Model):
    nama_seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
    nama_kegiatan = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return "[" + str(self.nama_seminar) + "] " + self.nama_kegiatan + " pada " + str(self.date)


