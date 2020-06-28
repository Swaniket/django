from django.urls import path
from . import views

#provide the list of mapping
urlpatterns = [
    path('', views.index, name = 'index')
]
