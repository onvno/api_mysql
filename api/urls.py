from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    # ex: /app/
    path('', views.index, name='index'),
]