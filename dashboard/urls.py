from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('search/', views.search, name='dashboard'),
    # path('login', views.login, name='login'),
]