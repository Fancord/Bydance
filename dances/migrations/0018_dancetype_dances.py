# Generated by Django 3.2.6 on 2021-11-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dances', '0017_rename_bgimg_mainpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='dancetype',
            name='dances',
            field=models.ManyToManyField(to='dances.Dance', verbose_name='Танцы'),
        ),
    ]
