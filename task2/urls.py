from django.urls import path
from .views import SalesApiView
from .views import HomeView

app_name = "task2"
urlpatterns = [
    path('api/', SalesApiView.as_view(), name='api'),
    path("", HomeView.as_view(), name="home"),
]
