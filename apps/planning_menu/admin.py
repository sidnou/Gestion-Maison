from django.contrib import admin

from .models import JourMenu, MenuSemaine, Menu


# Register your models here.

class JourMenuInline(admin.TabularInline):
    model = JourMenu
    extra = 0
    max_num = 7 # limite le nombre de jours par semaine à 7 jours


@admin.register(MenuSemaine)
class MenuSemaineAdmin(admin.ModelAdmin):
    inlines = [JourMenuInline]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass
