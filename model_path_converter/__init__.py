# -*- coding: utf-8 -*-
import re
from django.urls import register_converter
from django.urls.converters import get_converter, IntConverter

__author__ = """Daniel Hepper"""
__email__ = "daniel@consideratecode.com"
__version__ = "0.1.0"


def camel_to_snake(s):
    camel_to_snake_regex = r"((?<=[a-z0-9])[A-Z]|(?!^)(?<!_)[A-Z](?=[a-z]))"
    return re.sub(camel_to_snake_regex, r"_\1", s).lower()


def snake_to_camel(s):
    snake_to_camel_regex = r"(?:^|_)(.)"
    return re.sub(snake_to_camel_regex, lambda m: m.group(1).upper(), s)


class ModelConverterMixin:
    def get_queryset(self):
        if self.queryset:
            return self.queryset.all()
        return self.model.objects.all()

    def to_python(self, value):
        try:
            return self.get_queryset().get(**{self.field: super().to_python(value)})
        except self.model.DoesNotExist:
            raise ValueError

    def to_url(self, obj):
        return super().to_url(getattr(obj, self.field))


def register_model_converter(
    model, name=None, field="pk", base=IntConverter, queryset=None
):
    """
    Registers a custom path converter for a model.

    :param model: a Django model
    :param str name: name to register the converter as
    :param str field: name of the lookup field
    :param base: base path converter, either by name or as class
                 (optional, defaults to `django.urls.converter.IntConverter`)
    :param queryset: a custom querset to use (optional, defaults to
                     `model.objects.all()`)
    """
    if name is None:
        name = camel_to_snake(model.__name__)
        converter_name = "{}Converter".format(model.__name__)
    else:
        converter_name = "{}Converter".format(snake_to_camel(name))

    if isinstance(base, str):
        base = get_converter(base).__class__

    converter_class = type(
        converter_name,
        (
            ModelConverterMixin,
            base,
        ),
        {"model": model, "field": field, "queryset": queryset},
    )

    register_converter(converter_class, name)
