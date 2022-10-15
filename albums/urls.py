from django.urls import path 
from albums import views

urlpatterns = [
    path('', views.AlbumView.as_view()),
]