from django import forms

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from django.utils.safestring import mark_safe

from dances.models import Dance, DanceType, MainPage, DancePerfomance

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DanceAdminForm(forms.ModelForm):
    description = forms.CharField(label='Апісанне', widget=CKEditorUploadingWidget())

    class Meta:
        model = Dance
        fields = '__all__'


@admin.register(Dance)
class DanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'danceType')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'danceType__name')
    list_filter = ('danceType',)
    form = DanceAdminForm
    save_as = True
    fieldsets = (
        ("Main", {
            "fields": (("name", "danceType", "dancePerfomances"),)
        }),
        ("About", {
            "classes": ("collapse",),
            "fields": (("description",),)
         }),
        ('Funcion', {
            "fields": (("creator", "url", "draft"),)
        }),
    )


class DanceInLine(admin.TabularInline):
    model = Dance
    extra = 1


@admin.register(DanceType)
class DanceTypeAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'description')
    inlines = [DanceInLine]
    save_on_top = True


class DancePerfomanceAdminForm(forms.ModelForm):
    description = forms.CharField(label='Апісанне', widget=CKEditorUploadingWidget())

    class Meta:
        model = DancePerfomance
        fields = '__all__'


@admin.register(DancePerfomance)
class DancePerfomanceAdmin(ModelAdmin):
    list_display = ("name", "id")
    list_display_links = ('name', 'id')
    search_fields = ('name',)
    form = DancePerfomanceAdminForm


@admin.register(MainPage)
class MainPageAdmin(ModelAdmin):
    list_display = ('id', "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="50" heiht="60"')

    get_image.short_description = "Изображение"
