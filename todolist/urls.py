from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completed-tasks', views.completed_tasks, name='completed_tasks'),
    path('outstanding-tasks', views.outstanding_tasks, name='outstanding_tasks'),
]