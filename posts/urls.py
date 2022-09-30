from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostDiaryView

router = DefaultRouter()
router.register("", PostDiaryView)


urlpatterns = [
    path("", include(router.urls)),
]
