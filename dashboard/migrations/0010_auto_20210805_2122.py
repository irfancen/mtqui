# Generated by Django 3.2.3 on 2021-08-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210805_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='angkatan',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='fakultas',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='is_ketua',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='jurusan',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='line_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='no_hp',
            field=models.CharField(max_length=15),
        ),
    ]
