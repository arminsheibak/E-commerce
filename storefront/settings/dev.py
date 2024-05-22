from .common import *

SECRET_KEY = "OsOTfIEAPOFB7Clfwc5b7tMfrqjQA8ZmuoGecMP_1Dn6k_-0j4E"
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "storefront",
        "USER": "root",
        "PASSWORD": "armin2493",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 25

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
