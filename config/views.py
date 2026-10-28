from django.shortcuts import render


def index(request):
    context = {
        'Titre': " Gestion Maison -- Accueil",
    }

    return render(request, 'index.html', context)