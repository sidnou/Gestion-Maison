from django.db import models
from django.urls import reverse


# Create your models here.
class ListeCourse(models.Model):
    nom_liste_course = models.CharField(max_length=255, verbose_name="Nom de la liste de course")

    class Meta:
        verbose_name = "Liste de course"
        verbose_name_plural = "Listes de course"


    def __str__(self):
        return self.nom_liste_course

    def get_absolute_url(self):
        return reverse('listes_courses:detail', args=[str(self.id)])
class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255,unique=True, verbose_name="Nom de la catégorie")

class Article(models.Model):
    liste_course = models.ForeignKey(ListeCourse, on_delete=models.CASCADE)
    nom_article = models.CharField(max_length=255, verbose_name="Nom de l'article")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name="Categorie")
    quantite = models.IntegerField(verbose_name="Quantité")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
