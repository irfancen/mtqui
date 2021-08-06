from django.db import models

class Mentor(models.Model):
    nama_mentor = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_mentor

class Lomba(models.Model):
    nama_lomba = models.CharField(max_length=100)
    alias = models.CharField(max_length=20)
    image_url = models.TextField()
    about = models.TextField()
    start_date = models.DateField()
    finish_date = models.DateField()
    guidebook_link = models.CharField(max_length=200)
    nama_mentor = models.ManyToManyField(Mentor)

    def __str__(self):
        return self.nama_lomba

class LombaRule(models.Model):
    nama_lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    rule = models.TextField()

    def __str__(self):
        return "%s -> LombaRule: %s" % (str(self.nama_lomba), self.rule)

class TrainingLearnt(models.Model):
    nama_lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    learnt = models.TextField()

    def __str__(self):
        return "%s -> TrainingLearnt: %s" % (str(self.nama_lomba), self.learnt)

class TrainingTimeline(models.Model):
    nama_lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    timeline = models.DateField()
    active = models.BooleanField(null=True, blank=True, default=False)
    deskripsi = models.CharField(max_length=100)

    def __str__(self):
        return "%s -> TrainingTimeline: %s -> %s" % (str(self.nama_lomba), str(self.timeline), self.deskripsi)
