from django.urls import path
from . import views


urlpatterns = [
    path('portfolio', views.potfolio,name='potfolio'),
]
