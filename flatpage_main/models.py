from django.db import models
from django.contrib.flatpages.models import FlatPage
from ckeditor_uploader.fields import RichTextUploadingField


class NewFlatpage(models.Model):
    """Создание страниц основанных на Ckeditor"""
    flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
    """Добавляем необходимые поля"""
    description = RichTextUploadingField(verbose_name='Основной текстовый контент страницы', default='')
    text_block = RichTextUploadingField(verbose_name='Дополнительный блок текста', default='')

    def __str__(self):
        return self.flatpage.title

    class Meta:
        verbose_name = "Содержание страницы"
        verbose_name_plural = "Содержание страницы"
