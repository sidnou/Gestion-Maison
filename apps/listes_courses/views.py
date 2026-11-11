from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView

from apps.listes_courses.models import Article, Categorie, ListeCourse


class Articlelistview(ListView):
    model = Article
    template_name = "listes_courses/article_list.html"
    context_object_name = "articles"
class AricleDetailview(DetailView):
    model = Article
    template_name = "listes_courses/article_detail.html"
    context_object_name = "article"


class Articlecreateview(CreateView):
    model = Article
    template_name = "listes_courses/article_create.html"


class Categorielistview(ListView):
    model = Categorie
    template_name = "listes_courses/categorie_list.html"
    context_object_name = "categorie"


class Categoriecreateview(CreateView):
    model = Categorie
    template_name = "listes_courses/categorie_create.html"


class Listescourseslistview(ListView):
    model = ListeCourse
    template_name = "listes_courses/liste_course_list.html"
    context_object_name = "listes_courses"


class Listescoursescreateview(CreateView):
    model = ListeCourse
    template_name = "listes_courses/liste_course_create.html"
    fields = "__all__"

    success_url = reverse_lazy("liste_course_list")

    def get_success_url(self) -> str:
        return self.success_url
