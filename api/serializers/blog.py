from rest_framework import serializers
from blog.models import Category, Tag, Blog, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image', 'content']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'content', 'image', 'category', 'user', 'tags', 'views']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['blog', 'user', 'content']

