# Generated by Django 3.2.3 on 2021-07-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_kompetisi_peserta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kompetisi',
            name='peserta',
            field=models.ManyToManyField(blank=True, related_name='kompetisi', to='dashboard.Peserta'),
        ),
    ]
