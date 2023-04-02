from . import views
from django.urls import path

urlpatterns = [
    path('', views.subjects, name='subjects'),
    path('create-subject', views.createSubject, name='create-subject'),
    path('create-subject/create', views.create, name='create'),
    path('create-subject/cancel', views.cancel, name='cancel'),
    path('delete-subject', views.deleteSubject, name='delete-subject'),
    path('delete-subject/delete/<int:id>', views.delete, name='delete'),
    path('delete-subject/cancel-delete', views.cancelDelete, name='cancel-delete'),
    # path('details/<int:id>', views.details, name='course-details'),
    # path('edit-course/<int:id>', views.editCourse, name='edit-course'),
    # path('edit-course/<int:id>/edit', views.edit, name='edit'),
]