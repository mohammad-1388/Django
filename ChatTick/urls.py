from django.urls import path
from . import views

app_name = 'ChatTick'
urlpatterns = [
    path('home/', views.index, name='index'),
]
