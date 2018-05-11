=====
Usage
=====

To use Django Model Path Converter in a project with model `MyModel`::

    from model_path_converter import register_model_converter

    register_model_converter(MyModel)

Assuming you have a view `detail` that expects a `MyModel` instance as
parameter named `obj`, you can then use it to define a URL pattern::

    path('<my_model:obj>/', views.detail, name='detail'),

Here is a full example::

    from .models import MyModel

    app_name = 'my_app'
    urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<my_model:obj>/', views.detail, name='detail'),
    ]

The `register_model_converter` function takes several optional arguments.
