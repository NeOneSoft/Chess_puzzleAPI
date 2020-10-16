# Djangorestframework
from rest_framework import serializers

# Models
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    """
    Board general purpose serializer
    """

    class Meta:
        model = Board
        fields = ['id', 'board_size']


class CreateBoardSerializer(serializers.ModelSerializer):
    """
    Create Board serializer
    """

    class Meta:
        model = Board
        fields = ['board_size']