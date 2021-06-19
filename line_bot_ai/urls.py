from django.urls import path
from . import views
from .views import HomeList,Update,Delete

urlpatterns = [
    path('line', views.index, name='callback'),
    path('',HomeList.as_view(),name='form'),
    path('update/<int:pk>/',Update.as_view(),name='update'),
    path('delete/<int:pk>/',Delete.as_view(),name="delete")
]