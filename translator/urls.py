from django.urls import path
from .views import translate_binary

urlpatterns = [
    path('', translate_binary, name='translate_binary'),
]

