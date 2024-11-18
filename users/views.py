from django.shortcuts import render
from .models import User


# Create your views here.
def user_page(request, id):
    user = User.objects.get(id=id)
    return render(request, "users/user_page.html", {"user": user})


def user_followers(request, id):
    user = User.objects.get(id=id)
    followers = user.followers.all()
    return render(
        request, "users/user_followers.html", {"user": user, "followers": followers}
    )


def user_following(request, id):
    user = User.objects.get(id=id)
    following = user.following.all()
    return render(
        request, "users/user_following.html", {"user": user, "following": following}
    )
