from rest_framework import status
from rest_framework.response import Response

# from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .serializers import PostSerializers
from .permissions import PostPermission
from .models import Post
from .utils import get_query


# class PostViewSet(ModelViewSet):
#     """
#     일기장 CRUD
#     """

#     permission_classes = [PostPermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers


class PostView(APIView):

    permission_classes = [PostPermission]

    def post(self, request):
        serializer = PostSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "게시글 작성에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        offset = int(request.GET.get("offset", 0))
        limit = int(request.GET.get("limit", 10))

        post = Post.objects.all()[offset : offset + limit]

        serializer = PostSerializers(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):

    permission_classes = [PostPermission]

    def get(self, request, id):
        post = get_query(id)
        serializer = PostSerializers(post)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        post = self.get_query(id)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "SUCCESS"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
