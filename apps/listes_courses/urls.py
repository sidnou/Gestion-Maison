from django.urls import path

from .views import (
    Articlecreateview,
    Articledetailview,
    Articlelistview,
    Categoriecreateview,
    Categoriedetailview,
    Categorielistview,
    Listescoursescreateview,
    Listescoursesdetailview,
    Listescourseslistview,
)

urlpatterns = [
    path('', Listescourseslistview.as_view(), name='liste_course_list'),
    path('detail/', Listescoursesdetailview.as_view(), name='liste_course_detail'),
    path('add/', Listescoursescreateview.as_view(), name='liste_course_create'),
    path("articles/", Articlelistview.as_view(), name="article_list"),
    path("articles/detail/",Articledetailview.as_view(),name="article_detail"),
    path("articles/add/", Articlecreateview.as_view(),name="article_create"),
    path("categories/",Categorielistview.as_view(), name="categorie_list"),
    path("categories/detail/",Categoriedetailview.as_view(), name="categorie_detail"),
    path("categories/add/",Categoriecreateview.as_view(),name="categorie_create"),

]
