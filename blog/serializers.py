from rest_framework import serializers
from .models import Article, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'author_name', 'categories']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','created_at','author']