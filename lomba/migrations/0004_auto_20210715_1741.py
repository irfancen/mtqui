# Generated by Django 3.2.3 on 2021-07-15 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lomba', '0003_auto_20210714_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lombatimeline',
            name='lombaDetail',
        ),
        migrations.AddField(
            model_name='lomba',
            name='about',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lombatimeline',
            name='lomba',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='lomba.lomba'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LombaDetail',
        ),
    ]
