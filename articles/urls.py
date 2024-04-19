
from django.urls import path
from . import views 


app_name = "articles"

urlpatterns = [
    path("", views.articles, name="articles"),
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"), 
    #
    #
    path("data_throw/", views.data_throw, name="data_throw"),
    path("data_catch/", views.data_catch, name="data_catch"),
    path("hello/", views.hello, name="hello"),
]
