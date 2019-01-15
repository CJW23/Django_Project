from django.urls import path

from . import views

"""views.() <- 함수 이름"""
urlpatterns = [
    path('', views.index, name='index'),
]
