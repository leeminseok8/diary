from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostView, PostDetailView  # , PostViewSet

# router = DefaultRouter()
# router.register("post", PostViewSet)

urlpatterns = [
    # path("", include(router.urls)),
    path("", PostView.as_view),
    path("<int:id>", PostDetailView.as_view),
]
