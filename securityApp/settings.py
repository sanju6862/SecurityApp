import os
from pathlib import Path
import googlemaps
from channels import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+2ry*e$@*2u7o(3e&y%ytd!95j7l4nmfg^#lp!xsgkf*_cju44'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UserConfig',
    'complaints',
    'Emergency_contacts',
    'notifications',
    'incidentreporting',
    'LostFound',
    'django.contrib.gis',
    'announcements',
    'channels',
    'chat',
    'guidelines',
    'involvements',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'securityApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'securityApp.wsgi.application'
ASGI_APPLICATION = 'securityApp.routing.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'securityapp',
        'USER': 'ishwar1',
        'PASSWORD': 'Sanju#6862',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# import dj_database_url
# DATABASES = {
#     'default': dj_database_url.parse('postgres://ishwar:bvPljfupBYEWlTMJE3JoIcNz2lXzM7QL@dpg-civrai407spr6t9s3csg-a.oregon-postgres.render.com/securitysystem')
# }




# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Authentication
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "ishwarkumawat686222@gmail.com"
EMAIL_HOST_PASSWORD = "vbqqoexqdiglofaz"

# Session cookie age
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30

# Social authentication configurations for GitHub
SOCIAL_AUTH_GITHUB_KEY = str(os.getenv('GITHUB_KEY'))
SOCIAL_AUTH_GITHUB_SECRET = str(os.getenv('GITHUB_SECRET'))

# Social authentication configurations for Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "667057222669-tmm36ce6hlp9lm5h19rf4iov4bpu63lb.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

# Google Maps API key
GOOGLE_MAPS_API_KEY = 'AIzaSyBpOiF-121i2BcRBwWHg2ZSJxSl2QGsAwY'

gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
# settings.py
USER_LASTSEEN_TIMEOUT = 600  # 10 minutes
USER_ONLINE_TIMEOUT = 300  # 5 minutes
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}