from django.forms import ModelForm

from .models import Dance


class DanceForm(ModelForm):
    """Для создания танца на сайте"""
    class Meta:
        model = Dance
        fields = ['name', 'description', 'creator', 'danceType']
