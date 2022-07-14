#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `django_model_path_converter` package."""

from django.test import TestCase
from django.urls import path
from django.urls.converters import StringConverter
from django.urls.exceptions import Resolver404
from django.urls.resolvers import RegexPattern, URLResolver
from model_path_converter import register_model_converter

from example.blog.models import Article


def dummy_view(request, article):
    pass


class ModelConverterTestCase(TestCase):
    def resolve(self, path, pattern):
        url_resolver = URLResolver(RegexPattern(r"^/"), urlconf_name=[pattern])
        return url_resolver.resolve(path)

    def reverse(self, pattern, name, *args, **kwargs):
        url_resolver = URLResolver(RegexPattern(r"^/"), urlconf_name=[pattern])
        return url_resolver.reverse(name, *args, **kwargs)

    def assertNoMatch(self, path, pattern):
        with self.assertRaises(Resolver404):
            self.resolve(path, pattern)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.published_article = Article.objects.create(
            id=42,
            title="My Article",
            slug="my_article",
            content="Lorem ipsum etc",
            is_published=True,
        )
        cls.unpublished_article = Article.objects.create(
            id=99,
            title="Draft",
            slug="draft",
            content="This still needs some work",
            is_published=False,
        )

    def test_match(self):
        url = "/{}/".format(self.published_article.id)
        register_model_converter(Article)
        pattern = path("<article:article>/", dummy_view)
        match = self.resolve(url, pattern)
        self.assertEqual(match.kwargs["article"].id, self.published_article.id)
        self.assertEqual(
            url[1:], self.reverse(pattern, dummy_view, article=self.published_article)
        )

    def test_no_match(self):
        self.assertNoMatch("/43/", path("<article:article>/", dummy_view))

    def test_custom_name(self):
        url = "/{}/".format(self.published_article.id)
        register_model_converter(Article, name="my_article_converter")
        pattern = path("<my_article_converter:article>/", dummy_view)
        match = self.resolve(url, pattern)
        self.assertEqual(match.kwargs["article"].id, self.published_article.id)
        self.assertEqual(
            url[1:], self.reverse(pattern, dummy_view, article=self.published_article)
        )

    def test_custom_lookup_field(self):
        url = "/{}/".format(self.published_article.slug)
        register_model_converter(
            Article, name="article_from_slug", field="slug", base=StringConverter
        )
        pattern = path("<article_from_slug:article>/", dummy_view)
        match = self.resolve(url, pattern)
        self.assertEqual(match.kwargs["article"].id, self.published_article.id)
        self.assertEqual(
            url[1:], self.reverse(pattern, dummy_view, article=self.published_article)
        )

    def test_base_as_str(self):
        register_model_converter(
            Article, name="article_from_slug", field="slug", base="str"
        )
        match = self.resolve(
            "/{}/".format(self.published_article.slug),
            path("<article_from_slug:article>/", dummy_view),
        )
        self.assertEqual(match.kwargs["article"].id, self.published_article.id)

    def test_queryset(self):
        register_model_converter(
            Article,
            name="published_article",
            field="id",
            queryset=Article.objects.filter(is_published=True),
        )
        pattern = path("<published_article:article>/", dummy_view)
        match = self.resolve("/{}/".format(self.published_article.id), pattern)
        self.assertEqual(match.kwargs["article"].id, self.published_article.id)
        self.assertNoMatch("/{}/".format(self.unpublished_article.id), pattern)
