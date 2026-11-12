from django.db import models

from apps.core.utils import annee
from datetime import date

# Create your models here.
numero_semaine = date.today().isocalendar().week
prochaine_semaine = numero_semaine + 1
class Menu(models.Model):
    nom_menu = models.CharField(max_length=100)


    def __str__(self):
        return self.nom_menu

class MenuSemaine(models.Model):
    semaine = models.PositiveSmallIntegerField(default=prochaine_semaine)

    def __str__(self):
        return f"Semaine {self.semaine}"

class JourMenu(models.Model):
    menu_semaine = models.ForeignKey(MenuSemaine, on_delete=models.CASCADE, related_name="jours")
    jour = models.CharField(max_length=10, choices=annee.Jour)
    matin = models.ForeignKey(Menu, on_delete=models.CASCADE,verbose_name="Menu du matin", related_name="matin")
    midi = models.ForeignKey(Menu, on_delete=models.CASCADE,verbose_name="Menu du midi", related_name="midi")
    soir = models.ForeignKey(Menu, on_delete=models.CASCADE,verbose_name="Menu du soir", related_name="soir")

    def __str__(self):
        return self.jour



