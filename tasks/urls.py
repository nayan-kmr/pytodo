from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('<int:task_id>/upvote', views.complete, name='complete'),
]
