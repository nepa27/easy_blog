from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet,
                   basename='posts')
router_v1.register('groups', GroupViewSet,
                   basename='groups')
router_v1.register(r'posts/(?P<post_id>.+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/follow/', FollowViewSet.as_view()),
    path('v1/', include('djoser.urls.jwt')),
]
