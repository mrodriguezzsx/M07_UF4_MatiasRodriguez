from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_one, name='index_one'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
    path('user-form/', views.user_form, name='user_form'),
    path('update-user/<str:pk>/', views.user_update, name='user_update'),
]