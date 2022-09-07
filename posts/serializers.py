import re

from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6)

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError("최소 6자 이상 입력하세요.")
        elif re.search("[0-9]+", password) is None:
            raise serializers.ValidationError("최소 1개 이상의 숫자가 포함되어야 합니다.")
        return password

    class Meta:
        model = Post
        fields = ("id", "title", "content", "password")
