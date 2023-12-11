from django.contrib import admin

from tasks.models import Task, Tags


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content", "is_completed", "deadline",
    )


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
