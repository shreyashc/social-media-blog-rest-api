from django.db import IntegrityError
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework import filters

from .models import BlogPost, Comment, Like

from .serializers import (
    BlogPostSerializer,
    CommentSerializer,
    LikeSerializer
)

from .permissions import (
    IsOwnerOrReadOnly,
    CommentIsOwnerOrReadOnly,
    LikeIsOwnerOrReadOnly
)


class BlogViewSet(viewsets.ModelViewSet):

    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = BlogPost.objects.all()

        username = self.request.query_params.get('username', None)
        userid = self.request.query_params.get('userid', None)
        category = self.request.query_params.get('category', None)
        title = self.request.query_params.get('title', None)

        if username is not None:
            queryset = queryset.filter(author__username=username)
        if userid is not None:
            queryset = queryset.filter(author__id=userid)
        if category is not None:
            queryset = queryset.filter(category=category)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset

    def perform_create(self, serializer):
        serializer.patial = True
        serializer.save(author=self.request.user)


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CommentIsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = Comment.objects.all()
        post = self.request.query_params.get('post', None)
        if post is not None:
            queryset = queryset.filter(post__id=post)
        return queryset

    def perform_create(self, serializer):
        serializer.patial = True
        serializer.save(commented_by=self.request.user)


class LikeViewset(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, LikeIsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        queryset = Like.objects.all()
        post = self.request.query_params.get('post', None)
        if post is not None:
            queryset = queryset.filter(post__id=post)
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(LikeViewset, self).create(request, *args, **kwargs)
        except IntegrityError:
            json = {"error": "already liked"}
            raise ValidationError(json)

    def perform_create(self, serializer):
        serializer.patial = True
        serializer.save(liked_by=self.request.user)


class SearchListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']