from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .permissions import PostPermission
from .models import Post


class PostViewSet(ModelViewSet):
    """
    자유 게시판, 댓글 기능 포함
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)
        return super().perform_create(serializer)
