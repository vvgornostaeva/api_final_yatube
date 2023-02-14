from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)
from .permissions import IsAuthorOrReadOnly, ReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Метод создания поста с сохранением его автора."""
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """Метод определения прав доступа к постам

        Неавторизованный пользователь имеет доступ чтения одного поста
        или списка постов
        Авторизованный пользователь может создавать новые посты
        Авторизованный автор поста может его изменять, удалять.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return (ReadOnly(),)
        return super().get_permissions()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        """Метод получения queryset cо всеми комментариями поста."""
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post.comments.all()

    def perform_create(self, serializer):
        """Метод создания комментария с сохранением его автора."""
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)

    def get_permissions(self):
        """Метод определения прав доступа к комментариям

        Неавторизованный пользователь имеет доступ чтения одного комментария
        или списка комментариев
        Авторизованный пользователь может создавать новые комментарии
        Авторизованный автор комментария может его изменять, удалять.
        """
        if self.action == 'retrieve' or self.action == 'list':
            return (ReadOnly(),)
        if self.action == 'create':
            return (IsAuthenticated(),)
        return super().get_permissions()


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Follow."""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Метод получения queryset cо всеми подписками пользователя."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Метод создания подписки с сохранением пользователя."""
        serializer.save(user=self.request.user)
