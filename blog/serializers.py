from rest_framework import serializers
from users.models import BlogCustomUser
from .models import BlogPost, Comment, Like


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogCustomUser
        fields = ['id', 'username']
        read_only_fields = ['username']


class NestedCommentsSerializer(serializers.ModelSerializer):
    commented_by = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'commented_by']


class NestedLikesSerializer(serializers.ModelSerializer):

    liked_by = AuthorSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'liked_by']


class BlogPostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)
    comment = NestedCommentsSerializer(many=True, read_only=True)
    likes = NestedLikesSerializer(many=True, read_only=True)
    no_of_likes = serializers.SerializerMethodField()
    no_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost

        fields = ['id', 'author', 'title', 'category', 'description',
                  'content', 'thumbnail', 'created_at', 'no_of_likes', 'no_of_comments',
                  'comment', 'likes']

        read_only_fields = ['id', 'author', 'likes', 'comment', 'no_of_likes',
                            'no_of_comments', 'created_at']

        depth = 1

    def get_no_of_likes(self, obj):
        return obj.likes.count()

    def get_no_of_comments(self, obj):
        return obj.comment.count()


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'post', 'text', 'commented_by', 'commented_at']
        read_only_fields = ['id', 'commented_by', 'commented_at']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'post', 'liked_by', 'liked_at']
        read_only_fields = ['id', 'liked_by', 'liked_at']
