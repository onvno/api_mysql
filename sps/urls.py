from django.urls import path
from . import views

app_name = 'sps'
urlpatterns = [
    # ex: /sps/
    path('', views.index, name='index'),
]