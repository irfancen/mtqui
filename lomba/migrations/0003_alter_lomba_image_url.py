# Generated by Django 3.2.3 on 2021-08-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lomba', '0002_lomba_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lomba',
            name='image_url',
            field=models.TextField(blank=True, default='https://images.unsplash.com/photo-1519818187420-8e49de7adeef', null=True),
        ),
    ]