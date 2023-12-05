# Generated by Django 4.2.7 on 2023-12-04 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TM', '0003_eventview_likes_likedevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_artist', models.CharField(max_length=255)),
                ('favorite_genre', models.CharField(max_length=255)),
                ('preferred_timeframe_start', models.DateField()),
                ('preferred_timeframe_end', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]