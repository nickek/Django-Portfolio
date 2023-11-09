from django.urls import URLPattern, path, include
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
]