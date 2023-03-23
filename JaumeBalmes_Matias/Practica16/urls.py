from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_one, name='index_one'),
    path('teachers/', views.index, name='teachers'),
]