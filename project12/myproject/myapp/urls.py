from django.urls import path
from . import views

urlpatterns = [

    path('', views.demo,name='demo'),
    path('movies/<int:movie_id>/', views.details,name='details'),
    path('add/', views.add_movie,name='add_movie'),
    path('update/<int:movie_id>/', views.update,name='update'),
    path('delete/<int:movie_id>/', views.delete,name='delete')




]