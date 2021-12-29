from django.urls import path
from . import views


urlpatterns = [
    path('kodeeTrybee', views.kodeeTrybee,name='kodeeTrybee'),
]
