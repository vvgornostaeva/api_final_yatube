from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')
router.register(r'^follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt'))
]
