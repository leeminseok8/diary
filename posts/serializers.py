import re

from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from posts.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    """
    일기장 생성 시리얼라이저
    생성 시 비밀번호 validation과 암호화를 진행
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "whether",
            "password",
            "created_at",
            "updated_at",
        ]

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError("비밀번호는 최소 6자 이상 입력하세요.")
        elif re.search("[0-9]+", password) is None:
            raise serializers.ValidationError("비밀번호는 최소 1개 이상의 숫자가 포함되어야 합니다.")
        return self.password_hash(password)

    def password_hash(self, password):
        if password:
            re_password = make_password(password)
        return re_password
