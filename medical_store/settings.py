from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-this-key'

# DEBUG = True
DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pharmacy',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medical_store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pharmacy.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'medical_store.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'medical_store_db',
#         'USER': 'root',
#         'PASSWORD': 'Pass@123',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(
#         default='sqlite:///db.sqlite3',
#         conn_max_age=600
#     )
# }


DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = False

STATIC_URL = 'static/'


STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

