from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-le*bpc^-kbgt1cfeqzd3j2^0meezac!p%p$fwgi73c@!)ro8qn')

#Desarrollo True, Producción False
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ["*"] 

# Configuración de archivos estáticos RENDER
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'drf_spectacular',
    'galeria',
    'fechas',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 👈 Agrega esto
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'API_NUESTRAWEB.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'API_NUESTRAWEB.wsgi.application'

# --- Configuración de la Base de Datos ---

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'), conn_max_age=600, ssl_require=True)
}

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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "La API de Nuestra Web",
    "DESCRIPTION": "Documentación completa de la API de Nuestra Web, que permite el funcionamiento de la web que sirve como nuestro diario.",
    "VERSION": "1.0.0",
}

CORS_ALLOW_ALL_ORIGINS = True

# --- AUTO MIGRACIONES EN PRODUCCIÓN (solo Render Free) ---
import sys
if 'runserver' not in sys.argv:
    try:
        from django.core.management import call_command
        print("🚀 Ejecutando migraciones automáticamente en Render...")
        call_command('makemigrations', 'galeria', interactive=False)
        call_command('migrate', interactive=False)
        print("✅ Migraciones completadas correctamente.")
    except Exception as e:
        print("⚠️ Error ejecutando migraciones:", e)


DEBUG = True # Cambiar a False en producción