from django.urls import path

from . import views

app_name = "tasks" # Unique name for app

urlpatterns = [
    path("" , views.index, name = "index"),
    path("add", views.add,name = "add")
]