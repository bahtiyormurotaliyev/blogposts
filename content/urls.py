from django.urls import path 
from .views import contents


urlpatterns = [
    path('', contents, name='content')
]