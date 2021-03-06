# Generated by Django 3.2.3 on 2021-08-14 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_kompetisi_tipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='kompetisi',
            name='kapasitas_kelompok',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kompetisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kelompok', to='dashboard.kompetisi')),
            ],
        ),
    ]
