# Generated by Django 3.2.6 on 2021-09-01 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dances', '0006_dance_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dance',
            name='owner',
        ),
        migrations.AddField(
            model_name='dance',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Стваральнік'),
        ),
    ]
