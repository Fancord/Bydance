from django.contrib.auth.models import User
from django.db import models


class Dance(models.Model):
    """Модель танца"""
    name = models.CharField(max_length=100,
                            blank=True,
                            default="Назва танца",
                            verbose_name='Назва')
    description = models.TextField(blank=True,
                                   verbose_name='Апісанне')
    creator = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                null=True)
    danceType = models.ForeignKey('DanceType',
                                  blank=True,
                                  on_delete=models.PROTECT,
                                  verbose_name='Тып танца')
    dancePerfomances = models.ManyToManyField('DancePerfomance',
                                              blank=True,
                                              verbose_name='Выкананні танцаў')
    url = models.SlugField(max_length=130,
                           unique=True,
                           null=True)
    draft = models.BooleanField('Распрацоўка', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Танец'
        verbose_name_plural = 'Танцы'
        ordering = ['name']


class DanceType(models.Model):
    """Модель типа танца"""
    name = models.CharField(max_length=40,
                            db_index=True,
                            verbose_name='Тып танца')
    description = models.TextField(blank=True,
                                   verbose_name='Апісанне тыпу')
    dances = models.ManyToManyField(Dance,
                                    verbose_name='Танцы',
                                    blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тып танца'
        verbose_name_plural = 'Тыпы танцаў'
        ordering = ['name']


class DancePerfomance(models.Model):
    """
    Модель выполнения танца
    В данный, за счёт Ckeditor в Dance.description можно не использовать
    """
    name = models.CharField(max_length=40,
                            verbose_name='Выкананне танца')
    description = models.TextField(blank=True,
                                   verbose_name='Апісанне')
    nameforHTML = models.CharField(max_length=40,
                                   verbose_name='Для HTML')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Выкананне танца'
        verbose_name_plural = 'Выкананні танцаў'


class MainPage(models.Model):
    """Модель картинок для главной страницы"""
    url_height = models.PositiveIntegerField(null=True,
                                             blank=True)
    url_width = models.PositiveIntegerField(null=True,
                                            blank=True)
    img = models.ImageField(upload_to='bg_img',
                            height_field='url_height',
                            width_field='url_width')

    class Meta:
        verbose_name = 'Фота для галоўнай старонкі'
        verbose_name_plural = 'Фоткі для галоўнай старонкі'
