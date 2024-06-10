from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [IsAdminUser]
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, methods=['get'])
    def search_user(self, request):
        query = request.query_params.get('user')
        if query is None:
            return Response({'message':'Ничего не найдено'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(login__icontains = query)
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, methods=['get'])
    def search_post(self, request):
        query = request.query_params.get('post')
        if query is None:
            return Response({'message':'Ничего не найдено'}, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.filter(title__icontains = query)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def search_by_theme(self, request):
        query = request.query_params.get('id')
        if query is None:
            return Response({'message':'Ничего не найдено'}, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.filter(theme = query)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def like(self,request):
        query = request.query_params.get('id')
        if query is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = Post.objects.get(pk=query)
        post.reaction = post.reaction +1
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'])
    def dislike(self, request):
        query = request.query_params.get('id')
        if query is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = Post.objects.get(pk=query)
        post.reaction -= 1
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
        
        
    
# Create your views here.
