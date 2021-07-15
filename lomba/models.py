from django.db import models

class Mentor(models.Model):
    nama_mentor = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_mentor

class Lomba(models.Model):
    nama_lomba = models.CharField(max_length=100)
    about = models.TextField()
    mentor = models.ManyToManyField(Mentor)

    def __str__(self):
        return self.nama_lomba

class LombaRules(models.Model):
    lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    rule = models.TextField()

    def __str__(self):
        return "Rule " + str(self.lomba) + ": " + str(self.rule)

class LombaLearned(models.Model):
    lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    learned = models.TextField()

    def __str__(self):
        return "Learned " + str(self.lomba) + ": " + str(self.learned)

class LombaTimeline(models.Model):
    lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    timeline = models.DateField()
    deskripsi = models.CharField(max_length=100)

    def __str__(self):
        return "Timeline " + str(self.lomba) + ": " + str(self.timeline) + " -> " + self.deskripsi
