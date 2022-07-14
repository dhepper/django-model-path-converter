from django.urls import path
from model_path_converter import register_model_converter
from . import models, views


register_model_converter(models.Article)

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    # NOTE: our custom model converter is register under the name 'article'
    path("<article:article>", views.detail, name="detail"),
]
