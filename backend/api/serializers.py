"""Сериализаторы задач."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализаторы задач."""

    class Meta:
        """Мета Сериализатора задач."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
