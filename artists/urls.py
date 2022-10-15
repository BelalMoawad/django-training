from django.urls import path 
from artists import views

urlpatterns = [
     path('', views.ArtistView.as_view()),
     path("<str:id>", views.SingleArtistView.as_view()),
]