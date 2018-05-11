===============================================
Example project for Django Model Path Converter
===============================================

This project demonstrates the Django Model Path Converter packages. Its models
are also used in the tests of the package.

Usage
-----
Install requirements::

    pip install -r requirements.txt

Create database::

    python manage.py migrate

Create a user so you can access the admin interface::

    python manage.py createsuperuser

Run development server::

    python manage.py runserver

The application should now be accessible at http://localhost:8000.

You might want log into the admin with your newly created user and create some
articles: http://localhost:8000/admin/

Througout the code, there are a couple of comments marked with `NOTE` that
highlight the use of django-model-path-converter.