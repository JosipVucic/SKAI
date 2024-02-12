from django.urls import path

from .views import HomeView, SchedulingApiView

app_name = "task3"
urlpatterns = [
    path('api/', SchedulingApiView.as_view(), name='api'),
    path("", HomeView.as_view(), name="home"),
]