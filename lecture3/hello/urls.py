from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ivine", views.ivine, name="ivine"),
    path("<str:name>", views.greet,name = "greet"),
    path("david" , views.david, name = "david")
]