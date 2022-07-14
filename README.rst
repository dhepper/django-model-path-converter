===========================
Django Model Path Converter
===========================


.. image:: https://img.shields.io/pypi/v/django-model-path-converter.svg
        :target: https://pypi.python.org/pypi/django-model-path-converter

.. image:: https://github.com/dhepper/django-model-path-converter/actions/workflows/main.yml/badge.svg
        :target: https://github.com/dhepper/django-model-path-converter/actions/workflows/main.yml

.. image:: https://readthedocs.org/projects/django-model-path-converter/badge/?version=latest
        :target: https://django-model-path-converter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

The Django Model Path Converter package dynamically creates custom path converters for your models.

* Free software: MIT license
* Documentation: https://django-model-path-converter.readthedocs.io.
* Background story: https://consideratecode.com/django-model-path-converters

Quickstart
----------

Install the latest version::

    pip install django-model-path-converter

Import ```register_model_converter`` and your model in your ``urls.py``::

    from model_path_converter import register_model_converter
    from .models import MyModel

Register a converter for your model::

    register_model_converter(MyModel)

Use the new converter in your path definitions::

    path('<my_model:obj>/', views.my_view, name='my-view')

Your view ``my_view`` will now receive a ``MyModel`` instance as argument.

``register_model_converter`` accepts four additional, optional arguments:

* name (``str``) – name to register the converter as
* field (``str``) – name of the lookup field
* base – base path converter, either by name or as class (optional, defaults to `django.urls.converter.IntConverter``)
* queryset – a custom queryset to use (optional, defaults to ``model.objects.all()``)

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
