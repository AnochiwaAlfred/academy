from . import views
from django.urls import path

urlpatterns = [
    path('', views.lecturer, name='lecturer'),
    path('create-lecturer', views.createLecturer, name='create-lecturer'),
    path('create-lecturer/create', views.create, name='create'),
    path('create-lecturer/batch-create', views.batchCreate, name='batch-create'),
    path('create-lecturer/lecturer-list-template', views.lecturerListTemplate, name='lecturer-list-template'),
    path('create-lecturer/cancel', views.cancel, name='cancel'),
    path('delete-lecturer/<int:id>', views.deleteLecturer, name='delete-lecturer'),
    path('delete-lecturer/delete/<int:id>', views.delete, name='delete'),
    path('delete-lecturer/cancel-delete', views.cancelDelete, name='cancel-delete'),
    path('profile/<int:id>', views.profile, name='lecturer-profile'),
    path('edit-lecturer/<int:id>', views.editLecturer, name='edit-lecturer'),
    path('edit-lecturer/<int:id>/edit', views.edit, name='edit'),
]