"""Создание задачи админом."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Задача от админа."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
