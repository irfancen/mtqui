# Generated by Django 3.2.3 on 2021-08-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20210813_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadatafakultas',
            name='makara_image_code',
        ),
        migrations.AddField(
            model_name='metadatafakultas',
            name='makara',
            field=models.ImageField(null=True, upload_to='makara/'),
        ),
    ]