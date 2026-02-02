from django.shortcuts import render
from rest_framework import viewsets

from .models import Article, Category, Comment
from .serializers import ArticleSerializer, CategorySerializer, CommentSerializer, ArticleWriteSerializer


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ArticleWriteSerializer
        else:
            return ArticleSerializer



