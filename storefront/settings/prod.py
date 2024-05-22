from .common import *
import dj_database_url
import os

SECRET_KEY = os.environ("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = []

DATABASES = {"default": dj_database_url.config()}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 25

CORS_ALLOWED_ORIGINS = [
    "",
]
