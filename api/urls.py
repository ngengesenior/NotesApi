from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.urls import path

app_name = "api"

urlpatterns = [
    path('tasks/', views.TaskListAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
