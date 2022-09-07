from django.db import models

from utils.timestamp import TimeStampedModel


class Post(TimeStampedModel):
    """
    Post 글 생성을 위한 기본 모델
    """

    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    password = models.CharField(max_length=16)

    class Meta:
        db_table = "posts"
