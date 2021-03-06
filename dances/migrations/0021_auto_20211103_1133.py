# Generated by Django 3.2.6 on 2021-11-03 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dances', '0020_alter_dancetype_dances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dance',
            name='danceType',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='dances.dancetype', verbose_name='Тып танца'),
        ),
        migrations.AlterField(
            model_name='dance',
            name='description',
            field=models.TextField(blank=True, max_length=2500, verbose_name='Апісанне'),
        ),
        migrations.AlterField(
            model_name='dancetype',
            name='description',
            field=models.TextField(blank=True, verbose_name='Апісанне тыпу'),
        ),
    ]
