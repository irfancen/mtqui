# Generated by Django 3.2.3 on 2021-08-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery'),
        ),
    ]