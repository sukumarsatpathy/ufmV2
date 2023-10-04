from django.urls import path, include
from . import views

urlpatterns = [
    path('webSettings/', views.webSettingsView, name='webSettings'),
]