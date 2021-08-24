from django.urls import path, include
from . import views

urlpatterns = [
    path('matricula', views.matricula, name='matricula')

]