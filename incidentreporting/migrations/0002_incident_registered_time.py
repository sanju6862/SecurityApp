# Generated by Django 4.1.2 on 2023-06-26 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('incidentreporting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='registered_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
