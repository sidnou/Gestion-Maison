from django.db import models


class Jour(models.TextChoices):
    LUNDI = "LUNDI","Lundi"
    MARDI = "MARDI","Mardi"
    MERCREDI = "MERCREDI","Mercredi"
    JEUDI = "JEUDI","Jeudi"
    VENDREDI = "VENDREDI","Vendredi"
    SAMEDI = "SAMEDI","Samedi"
    DIMANCHE = "DIMANCHE","Dimanche"

class Journée(models.TextChoices):
    MATIN = "MATIN","Matin"
    MIDI = "MIDI","Midi"
    SOIR = "SOIR","Soir"