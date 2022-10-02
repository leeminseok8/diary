from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import CursorPagination

from .serializers import PostCreateSerializer
from .permissions import IsAuthorUser

from apps.posts.models import Post
from apps.service.whether import WhetherView


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

    def create(self, request):
        whether = WhetherView()
        diary_whether = whether.now_whether()

        diary_create_data = {
            "title": request.data["title"],
            "content": request.data["content"],
            "password": request.data["password"],
            "whether": diary_whether,
        }

        serializer = PostCreateSerializer(data=diary_create_data)

        if serializer.is_valid():
            serializer.save()

        return Response({"message": "일기장이 생성되었습니다."}, status=status.HTTP_201_CREATED)
