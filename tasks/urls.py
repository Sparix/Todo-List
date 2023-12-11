from django.urls import path

from tasks.views import (
    IndexView,
    TagsListView,
    CreateTaskView,
    CreateTagView,
    UpdateTagView,
    UpdateTaskView,
    change_status_tasks,
    delete_task,
    DeleteTagsView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="home-page"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("task/create/", CreateTaskView.as_view(), name="create-task"),
    path("tag/create/", CreateTagView.as_view(), name="create-tag"),
    path("tag/update/<int:pk>/", UpdateTagView.as_view(), name="update-tag"),
    path("task/update/<int:pk>/", UpdateTaskView.as_view(), name="update-task"),
    path("task/change/status/<int:pk>/", change_status_tasks, name="task-status"),
    path("task/delete/<int:pk>/", delete_task, name="task-delete"),
    path("tag/delete/<int:pk>/", DeleteTagsView.as_view(), name="tag-delete"),

]

app_name = "tasks"
