from django.urls import path
from hello_world.views import index, menu

urlpatterns = [
path('', index),
path('menu/', menu),
]