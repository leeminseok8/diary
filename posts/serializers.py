import re

from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, min_length=6)

    def PasswordValidator(password):
        if re.search("[0-9]+", password) is None:
            raise serializers.ValidationError("최소 1개 이상의 숫자가 포함되어야 합니다.")

    class Meta:
        model = Post
        fields = ("id", "title", "content", "pssword")
