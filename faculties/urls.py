from . import views
from django.urls import path

urlpatterns = [
    path('', views.faculties, name='faculties'),
    path('add-faculty', views.addFaculty, name='add-faculty'),
    path('add-faculty/add', views.add, name='add'),
    path('add-faculty/batch-add', views.batchAdd, name='batch-add'),
    path('add-faculty/faculty-list-template', views.facultyListTemplate, name='faculty-list-template'),
    path('add-faculty/cancel', views.cancel, name='cancel'),
    path('details/<int:id>', views.details, name='faculty-details'),
    path('delete-faculty/<int:id>', views.deleteFaculty, name='delete-faculty'),
    path('delete-faculty/delete/<int:id>', views.delete, name='delete'),
    path('delete-faculty/cancel-delete', views.cancelDelete, name='cancel-delete'),
    path('edit-faculty/<int:id>', views.editFaculty, name='edit-faculty'),
    path('edit-faculty/<int:id>/edit', views.edit, name='edit'),
]