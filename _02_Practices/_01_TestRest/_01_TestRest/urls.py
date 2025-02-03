from django.contrib import admin
from django.urls import path
from genericApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('students-info/', views.GetStudents.as_view()),
    path('students-info/', views.GET_POST_STUDENTS.as_view()),
    path('students-info/<int:pk>/', views.RUD_STUDENTS.as_view()),
]
