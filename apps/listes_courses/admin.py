from django.contrib import admin

from apps.listes_courses.models import ListeCourse, Article


# Register your models here.
@admin.register(ListeCourse)
class ListeCourseAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    list_filter = ('nom',)
    search_fields = ('nom',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    list_filter = ('nom',)
    search_fields = ('nom',)