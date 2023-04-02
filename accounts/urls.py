from . import views
from django.urls import path

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('add-user', views.addUser, name='add-user'),
    path('add-user/add', views.add, name='add'),
    path('delete-user/<int:id>', views.deleteUser, name='delete-user'),
    path('delete-user/delete/<int:id>', views.delete, name='delete'),
    path('edit-user/<int:id>', views.editUser, name='edit-user'),
    path('edit-user/<int:id>/edit', views.edit, name='edit'),
    path('cancel', views.cancel, name='cancel'),
    path('details/<int:id>', views.details, name='details'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]