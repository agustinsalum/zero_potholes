"""
Configuración principal de Django para el proyecto Zero Potholes.
Incluye: apps, base de datos, JWT, CORS, rutas, archivos estáticos, etc.
"""

# -------------------------------------------------------------------
#                     IMPORTS Y CONFIGURACIÓN BASE
# -------------------------------------------------------------------
from pathlib import Path
import environ

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Inicializar gestión de variables de entorno
env = environ.Env()
environ.Env.read_env()  # Leer archivo .env

# -------------------------------------------------------------------
#                   CONFIGURACIÓN GENERAL (DESARROLLO)
# -------------------------------------------------------------------
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=True)

# Hosts permitidos (frontend, proxy, etc.)
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["localhost", "127.0.0.1"]
)

# -------------------------------------------------------------------
#                          INSTALLED_APPS
# -------------------------------------------------------------------
INSTALLED_APPS = [
    # Django apps por defecto
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Apps externas
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt",

    # Apps del proyecto
    "zero_potholes_app",
]

# -------------------------------------------------------------------
#                           MIDDLEWARE
# -------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    # Habilita CORS para permitir acceso desde React/Vite
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------------------------------------------------------
#                        CONFIGURACIÓN CORS
# -------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Frontend Vite (React)
]

CORS_ALLOW_CREDENTIALS = True  # Habilita cookies y auth cross-origin

# -------------------------------------------------------------------
#                   AUTENTICACIÓN Y PERMISOS (DRF + JWT)
# -------------------------------------------------------------------
REST_FRAMEWORK = {
    # Autenticación por defecto → JWT
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),

    # Permiso por defecto → requiere login
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# Config extra de JWT (opcional pero recomendado)
from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

# -------------------------------------------------------------------
#                              URLs y TEMPLATES
# -------------------------------------------------------------------
ROOT_URLCONF = "zero_potholes.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Si usarás templates personalizados, agregarlos aquí
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "zero_potholes.wsgi.application"

# -------------------------------------------------------------------
#                           BASE DE DATOS
# -------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    }
}

# -------------------------------------------------------------------
#                    VALIDACIÓN DE CONTRASEÑAS
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------------------------------------------
#                   ARCHIVOS ESTÁTICOS Y MEDIA
# -------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------------------------------------------------
#                        INTERNACIONALIZACIÓN
# -------------------------------------------------------------------
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
#                  CONFIGURACIÓN FINAL DE DJANGO
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
