from . import views
from django.urls import path

urlpatterns = [
    path('', views.level, name='level'),
    path('add-level', views.addLevel, name='add-level'),
    path('add-level/add', views.add, name='add'),
    path('add-level/cancel', views.cancelAdd, name='cancel'),
    path('delete-level/<str:pk>', views.deleteLevel, name='delete-level'),
    path('delete-level/delete/<str:pk>', views.delete, name='delete'),
    path('delete/cancel-delete', views.cancelDelete, name='cancel-delete'), 
]