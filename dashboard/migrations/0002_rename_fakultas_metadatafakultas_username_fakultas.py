# Generated by Django 3.2.3 on 2021-07-15 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metadatafakultas',
            old_name='fakultas',
            new_name='username_fakultas',
        ),
    ]
