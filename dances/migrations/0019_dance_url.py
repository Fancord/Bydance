# Generated by Django 3.2.6 on 2021-11-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dances', '0018_dancetype_dances'),
    ]

    operations = [
        migrations.AddField(
            model_name='dance',
            name='url',
            field=models.SlugField(max_length=130, null=True, unique=True),
        ),
    ]