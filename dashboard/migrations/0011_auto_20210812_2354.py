# Generated by Django 3.2.3 on 2021-08-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20210805_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='peserta',
            name='file_cv',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='peserta',
            name='foto_ktm',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='peserta',
            name='screenshot_siak',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
