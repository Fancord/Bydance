from django.urls import path

from .views import MainPageView, DanceCreateView, DanceView, DanceTypeView

urlpatterns = [
    path('', MainPageView.as_view(), name='main-page-View'),
    path('dances/', DanceTypeView.as_view(), name='danceView'),
    path('dances/<str:slug>/', DanceView.as_view(), name='dance_detail'),
]

# url для создания танца path('add', DanceCreateView.as_view(), name='add')
