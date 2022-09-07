from rest_framework import permissions


class PostPermission(permissions.BasePermission):
    """
    일기장 생성, 조회 : 모두 가능
    일기장 수정, 삭제 : 비밀번호 인증 가능
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or "POST":
            return True
        else:
            request.password == obj.password
