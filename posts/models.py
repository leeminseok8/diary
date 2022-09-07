from django.db import models

from utils import TimeStampedModel


class Post(models.Model, TimeStampedModel):
    """
    Post 글 생성을 위한 기본 모델
    """

    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    password = models.CharField()

    class Meta:
        db_tables = "posts"
