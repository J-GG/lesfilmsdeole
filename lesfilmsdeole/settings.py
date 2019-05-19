"""
Django settings for lesfilmsdeole project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

SECRET_KEY = os.environ.get("LESFILMSDEOLE_SECRET_KEY", "2@o-yih2@c8&(q1wp@5sp12rljojvul7==4&sf00k+2td2tdaf")

DEBUG = os.environ.get("LESFILMSDEOLE_DEBUG").lower() == "true"

ALLOWED_HOSTS = os.environ.get("LESFILMSDEOLE_ALLOWED_HOSTS", "localhost").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'filer',
    'mptt',
    'ckeditor',
    'configuration',
    'onepage',
    'navbar',
    'home',
    'aboutus',
    'industries',
    'portfolio',
    'pricing',
    'equipment',
    'testimonials',
    'regulations',
    'contact',
    'partnership',
    'footer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]

ROOT_URLCONF = 'lesfilmsdeole.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lesfilmsdeole.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('LESFILMSDEOLE_DATABASE_ENGINE', "django.db.backends.postgresql_psycopg2"),
        'NAME': os.environ.get('LESFILMSDEOLE_DATABASE_NAME', "lesfilmsdeole"),
        'USER': os.environ.get('LESFILMSDEOLE_DATABASE_USER', "postgres"),
        'PASSWORD': os.environ.get('LESFILMSDEOLE_DATABASE_PASSWORD', "toor"),
        'HOST': os.environ.get('LESFILMSDEOLE_DATABASE_HOST', "localhost"),
        'PORT': os.environ.get('LESFILMSDEOLE_DATABASE_PORT', "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')

MEDIA_URL = "/uploads/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar': [
            {'name': 'document', 'items': ['Source', '-', 'Preview', 'Maximize']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        ],
    }
}

# Email settings
EMAIL_HOST = os.environ.get("LESFILMSDEOLE_EMAIL_HOST", "smtp.mailtrap.io")
EMAIL_HOST_USER = os.environ.get("LESFILMSDEOLE_EMAIL_HOST_USER", "44c56a0261a83f")
EMAIL_HOST_PASSWORD = os.environ.get("LESFILMSDEOLE_EMAIL_HOST_PASSWORD", "b21f7b699d7469")
EMAIL_PORT = os.environ.get("LESFILMSDEOLE_EMAIL_PORT", "2525")

GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get("LESFILMSDEOLE_GOOGLE_RECAPTCHA_SECRET_KEY")

# Activate Django-Heroku.
django_heroku.settings(locals())
