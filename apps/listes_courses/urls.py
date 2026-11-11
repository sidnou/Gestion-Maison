from django.urls import path

from .views import (
    Articlecreateview,
    Articlelistview,
    Categoriecreateview,
    Categorielistview,
    Listescoursescreateview,

    Listescourseslistview, AricleDetailview,
)

app_name = "listes_courses"
urlpatterns = [
    path('', Listescourseslistview.as_view(), name='liste_course_list'),
    path('add/', Listescoursescreateview.as_view(), name='liste_course_create'),
    path("articles/", Articlelistview.as_view(), name="article_list"),
    path("articles/add/", Articlecreateview.as_view(), name="article_create"),
    path("articles/<int:pk>/", AricleDetailview.as_view(), name="article_detail"),
    path("categories/", Categorielistview.as_view(), name="categorie_list"),
    path("categories/add/", Categoriecreateview.as_view(), name="categorie_create"),

]
