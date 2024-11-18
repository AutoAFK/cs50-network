from django.db import models
from users.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes")

    def get_likes_amount(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.body}"
