from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("new", views.new_post, name="new"),
    path("like", views.like_post, name="like"),
]
