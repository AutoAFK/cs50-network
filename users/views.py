from django.http import JsonResponse
from django.shortcuts import render
from .models import User


# Create your views here.
def user_page(request, id):
    user = User.objects.get(id=id)
    return render(request, "users/user_page.html", {"user": user})


def user_followers(request, id):
    user = User.objects.get(id=id)
    followers = user.user_followers.all()
    return render(
        request, "users/user_followers.html", {"user": user, "followers": followers}
    )


def user_following(request, id):
    user = User.objects.get(id=id)
    following = user.user_following.all()
    return render(
        request, "users/user_following.html", {"user": user, "following": following}
    )


def follow(request, id):
    current_user = User.objects.get(id=request.user.id)
    user_to_follow = User.objects.get(id=id)
    # removes the user if already following him
    if user_to_follow in current_user.user_following.all():
        current_user.user_following.remove(user_to_follow)
        user_to_follow.user_followers.remove(current_user)
        return JsonResponse({"status": 200, "action": "removed"})
    current_user.user_following.add(user_to_follow)
    user_to_follow.user_followers.add(current_user)
    return JsonResponse({"status": 200, "action": "added"})
