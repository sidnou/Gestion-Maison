from argparse import Action

from django.contrib import admin
from django.db import models
from apps.listes_courses.models import Article, Categorie, ListeCourse


# Register your models here.

class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom_article',)
    list_filter = ('nom_article',)
    search_fields = ('nom_article',)


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie',)
    list_filter = ('nom_categorie',)
    search_fields = ('nom_categorie',)


@admin.register(ListeCourse)
class ListeCourseAdmin(admin.ModelAdmin):
    list_display = ('nom_liste_course',)
    list_filter = ('nom_liste_course',)
    search_fields = ('nom_liste_course',)

    inlines = (
        ArticleInline,
    )
