from django.db import models
from django.urls import reverse


# Create your models here.
class ListeCourse(models.Model):
    nom = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Liste de course"
        verbose_name_plural = "Listes de courses"
        ordering = ['nom']

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('listes_courses:detail', args=[str(self.id)])


class Article(models.Model):
    liste_course = models.ForeignKey(ListeCourse, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255, unique=True)
    quantite = models.IntegerField()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['nom']