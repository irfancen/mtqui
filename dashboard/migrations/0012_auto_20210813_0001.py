# Generated by Django 3.2.3 on 2021-08-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210812_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='file_cv',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='foto_ktm',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='screenshot_siak',
            field=models.ImageField(upload_to=''),
        ),
    ]
