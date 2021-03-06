# Generated by Django 3.2.6 on 2021-08-30 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dances', '0003_auto_20210825_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='DanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40, verbose_name='Тып танца')),
            ],
        ),
        migrations.AlterModelOptions(
            name='dance',
            options={'ordering': ['name'], 'verbose_name': 'Танец', 'verbose_name_plural': 'Танцы'},
        ),
        migrations.RemoveField(
            model_name='dance',
            name='type',
        ),
        migrations.AlterField(
            model_name='dance',
            name='description',
            field=models.TextField(blank='True', max_length=2500, null='True', verbose_name='Апісанне'),
        ),
        migrations.AlterField(
            model_name='dance',
            name='name',
            field=models.CharField(blank='True', max_length=100, null='True', verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='dance',
            name='danceType',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.PROTECT, to='dances.dancetype', verbose_name='Тып танца'),
            preserve_default='True',
        ),
    ]
