# Generated by Django 4.1.2 on 2023-06-27 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LostFound', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='is_recovered',
            field=models.BooleanField(default=False),
        ),
    ]
