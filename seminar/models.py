from django.db import models
from django.utils import timezone

# Create your models here.
class GuestStars(models.Model):
    nama = models.CharField(max_length=150)

    def __str__(self):
        return self.nama

class Seminar(models.Model):
    judul_seminar = models.CharField(max_length=200)
    about = models.CharField(max_length=300)
    guest_stars = models.ManyToManyField(GuestStars)
    subjects = models.TextField()
    d_day = models.DateTimeField()
    seminar_image = models.ImageField(default='1955361.jpg')
    is_past = models.BooleanField(default=False)
    air_time = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.judul_seminar



