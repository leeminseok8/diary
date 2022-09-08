import re
import bcrypt

from rest_framework import serializers

from posts.models import Post


def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )
    return hashed_password


class PostSerializers(serializers.ModelSerializer):
    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError("최소 6자 이상 입력하세요.")
        elif re.search("[0-9]+", password) is None:
            raise serializers.ValidationError("최소 1개 이상의 숫자가 포함되어야 합니다.")
        return password

    def validate_title(self, title):
        if len(title) > 20:
            raise serializers.ValidationError("최대 20자까지 입력할 수 있습니다.")
        return title

    def validate_content(self, content):
        if len(content) > 200:
            raise serializers.ValidationError("최대 200자까지 입력할 수 있습니다.")
        return content

    def create(self, validated_data):
        password = validated_data.pop("tags", None)
        post = Post.objects.create(**validated_data)

        if password:
            post.password = hash_password(password)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.password = hash_password(validated_data.pop("password"))
        return super().update(instance, validated_data)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "password", "author")
