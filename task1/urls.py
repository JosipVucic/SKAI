from django.urls import path

from .views import HomeView

app_name = "task1"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]