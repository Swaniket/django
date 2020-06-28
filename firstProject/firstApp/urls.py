from django.urls import path
from . import views

#provide the list of mapping
urlpatterns = [
    path('', views.home, name = 'home'),
    path('add', views.add, name='add')
]
