from . import views
from django.urls import path

urlpatterns = [
    path('', views.courses, name='courses'),
    path('create-course', views.createCourse, name='create-course'),
    path('create-course/create', views.create, name='create'),
    path('create-course/cancel', views.cancel, name='cancel'),
    path('delete-course/<int:id>', views.deleteCourse, name='delete-course'),
    path('delete-course/delete/<int:id>', views.delete, name='delete'),
    path('delete-course/cancel-delete', views.cancelDelete, name='cancel-delete'),
    path('details/<int:id>', views.details, name='course-details'),
    path('edit-course/<int:id>', views.editCourse, name='edit-course'),
    path('edit-course/<int:id>/edit', views.edit, name='edit'),
    path('create-course/batch-create', views.batchCreate, name='batch-create'),
    path('create-course/course-list-template', views.courseListTemplate, name='course-list-template'),
]