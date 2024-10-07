from rest_framework import serializers
from .models import AITool, Creation, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AIToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = AITool
        fields = '__all__'

class CreationSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    tools_used = AIToolSerializer(many=True, read_only=True)

    class Meta:
        model = Creation
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'