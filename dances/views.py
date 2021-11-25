from django.views.generic import CreateView, ListView, DetailView

from dances.models import Dance, DanceType, MainPage

from .forms import DanceForm


class MainPageView(ListView):
    """Для сладйшоу на основной странице"""
    model = MainPage
    queryset = MainPage.objects.all()


class DanceView(DetailView):
    """Вывод информации об танце"""
    model = Dance
    queryset = Dance.objects.filter(draft=False)
    slug_field = 'name'


class DanceTypeView(ListView):
    """Выводит список типов танцев"""
    model = DanceType
    queryset = DanceType.objects.all()
    template_name = "dances/dance_section.html"


class DanceCreateView(CreateView):
    """
    Для создания модели танца на самом сайте
    Необходимо добавить path в urls.py
    """
    template_name = 'dances/create.html'
    form_class = DanceForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['danceTypes'] = DanceType.objects.all()
        return context
