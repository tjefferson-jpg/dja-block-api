from  django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CategoryViewSet, CommentViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]