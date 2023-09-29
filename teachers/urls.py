from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teachers_view/", views.teachers_view, name="teachers view"),
]
