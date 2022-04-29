from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet, TagModelViewSet, BlogListCreateAPIView, BlogModelViewSet, RegisterAPIView, CommentViewSet, LoginAPIView

router = DefaultRouter()
router.register('category', CategoryModelViewSet)
router.register('tag', TagModelViewSet)
router.register('comment', CommentViewSet)
router.register('blog', BlogModelViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path('blog', BlogListCreateAPIView.as_view(), name='blog'),
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
]
