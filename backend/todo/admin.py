from django.contrib import admin
from .models import TodoItem


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['label', 'done', 'created']
    list_filter = ['done', 'created']
    list_editable = ['done']
    search_fields = ['label']
    ordering = ['created']
