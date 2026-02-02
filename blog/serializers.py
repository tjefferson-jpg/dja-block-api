from rest_framework import serializers

from account.serializers import UserViewSerializer
from .models import Article, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','created_at','author']

"""
class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'author_name', 'categories']
        # depth = 1 permet de transformer les IDs en objets complets automatiquement
"""


class ArticleWriteSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'author_name', 'categories']

class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author = UserViewSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'author_name', 'categories']

