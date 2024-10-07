from rest_framework import viewsets
from .models import AITool, Creation, Comment
from .serializers import AIToolSerializer, CreationSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

class AIToolViewSet(viewsets.ModelViewSet):
    queryset = AITool.objects.all()
    serializer_class = AIToolSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreationViewSet(viewsets.ModelViewSet):
    queryset = Creation.objects.all()
    serializer_class = CreationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        creation = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creation=creation, author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)