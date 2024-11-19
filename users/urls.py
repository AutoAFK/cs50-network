from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("<int:id>", views.user_page, name="user_page"),
    path("<int:id>/followers", views.user_followers, name="followers"),
    path("<int:id>/following", views.user_following, name="following"),
    path("<int:id>/follow", views.follow, name="follow"),
]
