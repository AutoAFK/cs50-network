import json
from django.shortcuts import redirect
from django.urls import reverse
from network.forms import PostForm
from django.http import JsonResponse
from .models import Post

# Create your views here.


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
