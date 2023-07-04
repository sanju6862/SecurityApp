# Generated by Django 4.1.2 on 2023-06-27 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('item_type', models.CharField(choices=[('card', 'Card'), ('keys', 'Keys'), ('purse', 'Purse'), ('mobile', 'Mobile'), ('watch', 'Watch'), ('other', 'Other')], max_length=20)),
                ('other_type', models.CharField(max_length=100, null=True)),
                ('media', models.FileField(blank=True, null=True, upload_to='item_media/')),
                ('recovered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recovered_items', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]