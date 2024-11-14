import json

from django.contrib.auth import authenticate, login, logout
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import PostForm
from .models import Post, User


def index(request):
    form = PostForm()
    posts = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page", 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "network/index.html", {"form": form, "posts": posts})


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            post_body = form.cleaned_data["post_body"]
            post = Post(user=user, body=post_body)
            post.save()
            return JsonResponse(
                {"success": True, "redirect_url": reverse("network:index")}
            )
        return JsonResponse(
            {"error": "Input is not valid, must contain 30 letters minimum."}
        )
    else:
        return redirect("network:index")


def like_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get("post_id")
        post = Post.objects.get(id=post_id)
        json_response = {"status": 200}
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            json_response["liked"] = False
        else:
            post.likes.add(request.user)
            json_response["liked"] = True
        json_response["liked_amount"] = post.get_likes_amount()
        return JsonResponse(json_response)


def user_page(request, id):
    user = User.objects.get(id=id)
    return render(request, "network/user/user_page.html", {user: user})


def user_followers(request, id):
    user = User.objects.get(id=id)
    followers = user.followers.all()
    return render(
        request, "network/user/user_followers.html", {user: user, followers: followers}
    )


def user_following(request, id):
    user = User.objects.get(id=id)
    following = user.following.all()
    return render(
        request, "network/user/user_following.html", {user: user, following: following}
    )


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("network:index"))
        else:
            return render(
                request,
                "network/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("network:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "network/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "network/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("network:index"))
    else:
        return render(request, "network/register.html")
