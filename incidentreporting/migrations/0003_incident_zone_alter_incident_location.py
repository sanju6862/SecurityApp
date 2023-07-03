# Generated by Django 4.1.2 on 2023-07-02 14:24

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('incidentreporting', '0002_incident_registered_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='zone',
            field=models.CharField(choices=[('near LC', 'Near LC'), ('near gymkhana', 'Near Gymkhana'), ('near rajputana', 'Near Rajputana'), ('near newgirls hostel', 'Near Newgirls Hostel')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incident',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
