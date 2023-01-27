from django.urls import path
from app2.views import dashboard

urlpatterns = [
    path("",dashboard, name="dashboard"),
]
