# Generated by Django 3.2.6 on 2021-08-30 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dances', '0004_auto_20210830_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dancetype',
            options={'ordering': ['name'], 'verbose_name': 'Тып танца', 'verbose_name_plural': 'Тыпы танцаў'},
        ),
    ]
