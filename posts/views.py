from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import CursorPagination

from .serializers import PostCreateSerializer
from .permissions import IsAuthorUser

from .models import Post


class ProductPagination(CursorPagination):
    """
    20개 씩 불러오는 페이지네이션
    sns같은 빈번한 CRUD가 빈번하게 일어나지 않지만 최신화를 위해 적용
    """

    page_size = 20
    ordering = "-created_at"


class PostDiaryView(ModelViewSet):
    """
    게시글 CRUD 기능
    perform_create를 통해 게시글 생성 시 게시자 등록
    """

    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostCreateSerializer
    pagination_class = ProductPagination
    permission_classes = (IsAuthorUser,)
