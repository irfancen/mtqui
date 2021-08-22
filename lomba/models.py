from django.db import models

class Mentor(models.Model):
    nama_mentor = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_mentor

class Lomba(models.Model):
    nama_lomba = models.CharField(max_length=100)
    alias = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True, default='https://images.unsplash.com/photo-1519818187420-8e49de7adeef')
    about = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    guidebook_link = models.CharField(max_length=200, default='/guidebook')
    nama_mentor = models.ManyToManyField(Mentor, null=True, blank=True)
    custom_timeline = models.BooleanField(default=False)

    def __str__(self):
        return self.nama_lomba

class LombaRule(models.Model):
    nama_lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    rule = models.TextField()

    def __str__(self):
        return "%s -> LombaRule: %s" % (str(self.nama_lomba), self.rule)

class ParticipantRequirement(models.Model):
    nama_lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    requirement = models.TextField()

    def __str__(self):
        return "%s -> ParticipantRequirement: %s" % (str(self.nama_lomba), self.requirement)

class TrainingLearnt(models.Model):
    nama_lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    learnt = models.TextField()

    def __str__(self):
        return "%s -> TrainingLearnt: %s" % (str(self.nama_lomba), self.learnt)

class TrainingTimeline(models.Model):
    nama_lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()
    active = models.BooleanField(null=True, blank=True, default=False)
    deskripsi = models.CharField(max_length=100)

    def __str__(self):
        return "%s -> TrainingTimeline: %s - %s -> %s" % (str(self.nama_lomba), str(self.start_date), str(self.finish_date), self.deskripsi)
