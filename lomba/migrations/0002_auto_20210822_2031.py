# Generated by Django 3.2.3 on 2021-08-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lomba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lomba',
            name='finish_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lomba',
            name='guidebook_link',
            field=models.CharField(default='/guidebook', max_length=200),
        ),
        migrations.AlterField(
            model_name='lomba',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
