from django.shortcuts import render
from .models import Article


def index(request):
    return render(request, "blog/index.html", {"articles": Article.objects.all()})


def detail(request, article):
    # NOTE: The view receives an actual Article object
    return render(request, "blog/detail.html", {"article": article})
