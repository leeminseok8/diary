from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.hashers import check_password


class IsAuthorUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        생성, 죄회 : 모든 유저 권한 부여
        수정, 삭제 : 비밀번호
        """

        if request.method in SAFE_METHODS:
            return True
        elif request.method == "POST":
            return True
        elif request.method in ("PATCH", "PUT", "DELETE"):
            return check_password(request.data["password"], obj.password)
