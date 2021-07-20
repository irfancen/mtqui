# Generated by Django 3.2.3 on 2021-07-15 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestStars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_seminar', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=300)),
                ('received', models.CharField(max_length=500)),
                ('requirement', models.CharField(max_length=500)),
                ('guest_stars', models.ManyToManyField(to='seminar.GuestStars')),
            ],
        ),
        migrations.CreateModel(
            name='EventDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kegiatan', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('nama_seminar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminar.seminar')),
            ],
        ),
    ]