"""
Configuración de Django para el proyecto zero_potholes
"""

from pathlib import Path
import environ

# Construí rutas dentro del proyecto de esta forma: BASE_DIR / 'subcarpeta'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Crear el archivo .env al mismo nivel que settings.py
env = environ.Env()
environ.Env.read_env()

# Configuración rápida para desarrollo: no apta para producción

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = []

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # Evita repetir permission_classes = [IsAuthenticated] en cada ViewSet
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# Definición de la aplicación
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zero_potholes_app',
    'rest_framework'
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

ROOT_URLCONF = 'zero_potholes.urls'

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

WSGI_APPLICATION = 'zero_potholes.wsgi.application'

# Base de datos
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

# Validación de contraseñas
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

# Internacionalización
LANGUAGE_CODE = 'es-ar'   # Español de Argentina
TIME_ZONE = 'America/Argentina/Buenos_Aires'  # Zona horaria de Buenos Aires
USE_I18N = True  # Internacionalización activada
USE_TZ = True    # Soporte para zonas horarias activado

# Archivos estáticos (CSS, JavaScript, imágenes)
STATIC_URL = 'static/'

# Tipo de campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'