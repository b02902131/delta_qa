from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # /ask/5/valid/
    path('valid/', views.valid, name='valid'),
]
