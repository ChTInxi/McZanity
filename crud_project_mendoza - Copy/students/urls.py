from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='list'),
    path('student/add/', views.StudentCreateView.as_view(), name='add'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='detail'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='edit'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='delete'),
]
