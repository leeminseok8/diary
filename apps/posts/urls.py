from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.posts.views import PostDiaryView

router = DefaultRouter()
router.register("", PostDiaryView)


urlpatterns = [
    path("", include(router.urls)),
]
