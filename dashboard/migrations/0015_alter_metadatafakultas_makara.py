# Generated by Django 3.2.3 on 2021-08-14 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20210814_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadatafakultas',
            name='makara',
            field=models.ImageField(upload_to='makara/'),
        ),
    ]
