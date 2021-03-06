# Generated by Django 3.2.3 on 2021-07-27 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_rename_fakultas_metadatafakultas_username_fakultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peserta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('npm', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kompetisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('kuota', models.IntegerField()),
                ('deadline_pendaftaran', models.DateField()),
                ('fakultas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kompetisi', to=settings.AUTH_USER_MODEL)),
                ('peserta', models.ManyToManyField(related_name='kompetisi', to='dashboard.Peserta')),
            ],
        ),
    ]
