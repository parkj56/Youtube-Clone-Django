from rest_framework import serializers
from .models import Replies
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'message', 'likes', 'dislikes', 'video']

class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ['id', 'comment', 'message']