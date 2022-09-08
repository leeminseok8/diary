import bcrypt

from rest_framework import status
from rest_framework.response import Response

from .models import Post


def get_query(self, id):
    try:
        query = Post.objects.get(id=id)
        return query
    except Post.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)


def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )
    return hashed_password
