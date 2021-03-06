# Generated by Django 3.2.3 on 2021-07-29 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_peserta_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kompetisi',
            name='peserta',
        ),
        migrations.AddField(
            model_name='peserta',
            name='kompetisi',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='peserta', to='dashboard.kompetisi'),
        ),
        migrations.AlterUniqueTogether(
            name='peserta',
            unique_together=set(),
        ),
    ]
