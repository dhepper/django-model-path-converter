SECRET_KEY = 'not_so_secret'

INSTALLED_APPS = [
    'example.blog'
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}