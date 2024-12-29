from django.contrib import admin
from django.urls import path
from . import views
from . views import TaskListView
from . views import TaskDetailView
from . views import TaskUpdateView



urlpatterns = [
    path('',views.task_view,name='task_view'),
    path('cbvtask/',views.TaskListView.as_view(),name='cbvtask'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),

]


