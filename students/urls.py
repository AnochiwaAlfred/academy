from . import views
from django.urls import path

urlpatterns = [
    path('', views.studentsPage, name='students-page'),
    path('add-student', views.addStudent, name='add-student'),
    path('add-student/add', views.add, name='add'),
    path('add-student/student-list-template', views.studentListTemplate, name='student-list-template'),
    path('add-student/cancel', views.cancel, name='cancel'),
    path('student/<int:id>', views.studentProfile, name='student-profile'),
    path('student/<int:id>/delete', views.deleteStudent, name='delete-student'),
    path('student/<int:id>/delete/confirm', views.delete, name='delete'),
    path('student/<int:id>/cancel-delete', views.cancelDelete, name='cancel-delete'),
    path('edit-student/<int:id>', views.editStudent, name='edit-student'),
    path('edit-student/<int:id>/edit', views.edit, name='edit'),
    path('students-list-csv', views.studentsListCsv, name='students-list-csv'),
    path('students-list-pdf', views.studentsListPdf, name='students-list-pdf'),
    path('add-student/batch-add', views.batchAdd, name='batch-add'),
]