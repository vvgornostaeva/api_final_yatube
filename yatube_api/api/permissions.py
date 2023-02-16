from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Класс определяет доступ в зависимости от авторства

    Автор объекта может создавать, изменять, удалять объекты
    Не автор может применять методы 'GET', 'HEAD', 'OPTIONS'.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
