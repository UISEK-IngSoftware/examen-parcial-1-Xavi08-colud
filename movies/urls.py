from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name = "index"),
    path("movie/<int:id>/", views.movie, name="movie" ),
    path("movie/add/", views.add_movie, name="add_movies" )
]

