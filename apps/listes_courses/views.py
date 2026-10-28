from django.views.generic import CreateView, DetailView, ListView

from apps.listes_courses.models import Article, Categorie, ListeCourse


class Articlelistview(ListView):
    model = Article
    template_name = "listes_courses/article_list.html"
    context_object_name = "articles"


class Articledetailview(DetailView):
    model = Article
    template_name = "listes_courses/article_detail.html"


class Articlecreateview(CreateView):
    model = Article
    template_name = "listes_courses/article_create.html"

class Categorielistview(ListView):
    model = Categorie
    template_name = "listes_courses/categorie_list.html"
    context_object_name = "categorie"
class Categoriedetailview(DetailView):
    model = Categorie
    template_name = "listes_courses/categorie_detail.html"
class Categoriecreateview(CreateView):
    model = Categorie
    template_name = "listes_courses/categorie_create.html"
class Listescourseslistview(ListView):
    model = ListeCourse
    template_name = "listes_courses/liste_course_list.html"
    context_object_name = "liste_courses"


# Create your views here.
class Listescoursesdetailview(DetailView):
    model = ListeCourse
    template_name = "listes_courses/liste_course_detail.html"
    context_object_name = "liste_course"


class Listescoursescreateview(CreateView):
    model = ListeCourse
    template_name = "listes_courses/liste_course_create.html"
    fields = "__all__"
