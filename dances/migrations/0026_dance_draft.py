# Generated by Django 3.2.6 on 2021-11-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dances', '0025_auto_20211103_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='dance',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Распрацоўка'),
        ),
    ]
