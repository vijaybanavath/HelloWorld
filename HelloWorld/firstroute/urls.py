from django.urls import path
from .views import View

urlpatterns = [
    path("",View, name="home"),
]
