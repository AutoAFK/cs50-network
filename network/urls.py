from django.urls import path

from . import views

app_name = "network"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts/new", views.new_post, name="posts/new"),
    path("posts/like", views.like_post, name="posts/like"),
    path("user/<int:id>", views.user_page, name="user/user_page"),
    path("user/<int:id>/followers", views.user_followers, name="user/followers"),
    path("user/<int:id>/following", views.user_following, name="user/following"),
]
