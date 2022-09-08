from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

from utils.timestamp import TimeStampedModel


class Post(TimeStampedModel):
    """
    Post 글 생성을 위한 기본 모델
    """

    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    password = models.CharField(max_length=128)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = "posts"
        ordering = ["-created_at"]
