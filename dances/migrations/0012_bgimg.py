# Generated by Django 3.2.6 on 2021-10-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dances', '0011_auto_20210920_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bgimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='bg_img')),
            ],
            options={
                'verbose_name': 'Фота для галоўнай старонкі',
                'verbose_name_plural': 'Фоткі для галоўнай старонкі',
            },
        ),
    ]
