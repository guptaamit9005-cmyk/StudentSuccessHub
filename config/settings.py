"""
Django settings for config project.

Production-ready configuration for:
- Local development
- Render deployment
- PostgreSQL
- WhiteNoise static files
- Environment variables
- CKEditor
- Custom User model
"""

from pathlib import Path
import os


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# ENVIRONMENT VARIABLES
# =========================================================

# Render automatically provides RENDER in production.
ON_RENDER = os.environ.get("RENDER") == "true"


# =========================================================
# SECURITY
# =========================================================

# IMPORTANT:
# Never hard-code your production SECRET_KEY in this file.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-local-development-only-change-me"
)


# DEBUG
#
# Local:
#     DEBUG=True
#
# Render:
#     DEBUG=False
#
DEBUG = os.environ.get(
    "DEBUG",
    "False" if ON_RENDER else "True"
).lower() == "true"


# =========================================================
# ALLOWED HOSTS
# =========================================================

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "ALLOWED_HOSTS",
        ""
    ).split(",")
    if host.strip()
]


# Render automatically provides the external hostname.
RENDER_EXTERNAL_HOSTNAME = os.environ.get(
    "RENDER_EXTERNAL_HOSTNAME"
)

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(
        RENDER_EXTERNAL_HOSTNAME
    )


# Local development
if not ON_RENDER:
    ALLOWED_HOSTS.extend([
        "127.0.0.1",
        "localhost",
    ])


# Remove duplicate hosts
ALLOWED_HOSTS = list(
    dict.fromkeys(ALLOWED_HOSTS)
)


# =========================================================
# INSTALLED APPS
# =========================================================

INSTALLED_APPS = [

    # -----------------------------------------------------
    # Django Apps
    # -----------------------------------------------------

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",


    # -----------------------------------------------------
    # Third Party Apps
    # -----------------------------------------------------

    "ckeditor",
    "ckeditor_uploader",


    # -----------------------------------------------------
    # Local Apps
    # -----------------------------------------------------

    "accounts",
    "notices",
    "resources",
    "collaboration",
    "academic_tracker",
    "grade_calculator",
    "daily_planner",
    "coding_contest",
    "lab_resources",
    "roadmap",
    "placement_support",
    "learning_hub",
    "students",
    "tutorials",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise
    # Must be immediately after SecurityMiddleware.
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URL CONFIGURATION
# =========================================================

ROOT_URLCONF = "config.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [

    {
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.debug",

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = "config.wsgi.application"


# =========================================================
# DATABASE
# =========================================================

# Production:
#     Render PostgreSQL using DATABASE_URL
#
# Local:
#     SQLite database

DATABASE_URL = os.environ.get(
    "DATABASE_URL"
)


if DATABASE_URL:

    try:

        import dj_database_url

        DATABASES = {
            "default": dj_database_url.parse(
                DATABASE_URL,
                conn_max_age=600,
                conn_health_checks=True,
            )
        }

    except ImportError:

        # This should never happen after deployment
        # if dj-database-url is in requirements.txt.

        DATABASES = {
            "default": {
                "ENGINE":
                    "django.db.backends.sqlite3",

                "NAME":
                    BASE_DIR / "db.sqlite3",
            }
        }

else:

    # -----------------------------------------------------
    # Local Development Database
    # -----------------------------------------------------

    DATABASES = {

        "default": {

            "ENGINE":
                "django.db.backends.sqlite3",

            "NAME":
                BASE_DIR / "db.sqlite3",
        }
    }


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator",
    },
]


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"


# Source static directory
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# Production collected static files
STATIC_ROOT = BASE_DIR / "staticfiles"


# WhiteNoise compressed static files
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# =========================================================
# MEDIA FILES
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# IMPORTANT:
#
# Render's default filesystem is ephemeral.
#
# Therefore, do NOT rely on local MEDIA_ROOT for
# permanent production PDF/image storage.
#
# For your Student Success Hub we can later use:
#
#     Google Drive
#     Cloudinary
#     AWS S3
#     Another persistent storage provider
#
# Google Drive links are especially suitable for
# educational PDFs/resources.


# =========================================================
# CKEDITOR
# =========================================================

CKEDITOR_UPLOAD_PATH = "tutorial_uploads/"


CKEDITOR_CONFIGS = {

    "default": {

        "toolbar": "full",

        "height": 400,

        "width": "100%",
    },
}


# =========================================================
# CUSTOM USER MODEL
# =========================================================

AUTH_USER_MODEL = "accounts.User"


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)


# =========================================================
# AUTHENTICATION REDIRECTS
# =========================================================

LOGIN_URL = "/login/"

LOGIN_REDIRECT_URL = "/dashboard/"

LOGOUT_REDIRECT_URL = "/"


# =========================================================
# CSRF / HTTPS SECURITY
# =========================================================

CSRF_TRUSTED_ORIGINS = []


if RENDER_EXTERNAL_HOSTNAME:

    CSRF_TRUSTED_ORIGINS.append(
        f"https://{RENDER_EXTERNAL_HOSTNAME}"
    )


# Optional custom domains
CUSTOM_DOMAIN = os.environ.get(
    "CUSTOM_DOMAIN"
)

if CUSTOM_DOMAIN:

    CSRF_TRUSTED_ORIGINS.append(
        f"https://{CUSTOM_DOMAIN}"
    )


# =========================================================
# PRODUCTION SECURITY SETTINGS
# =========================================================

if not DEBUG:

    # HTTPS
    SECURE_SSL_REDIRECT = True

    # Secure cookies
    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    # HSTS
    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    # Browser security
    SECURE_CONTENT_TYPE_NOSNIFF = True

    SECURE_REFERRER_POLICY = (
        "same-origin"
    )

    X_FRAME_OPTIONS = "DENY"


# =========================================================
# DEVELOPMENT SECURITY
# =========================================================

else:

    SECURE_SSL_REDIRECT = False

    SESSION_COOKIE_SECURE = False

    CSRF_COOKIE_SECURE = False


# =========================================================
# LOGGING
# =========================================================

LOGGING = {

    "version": 1,

    "disable_existing_loggers": False,

    "handlers": {

        "console": {

            "class":
                "logging.StreamHandler",
        },
    },

    "root": {

        "handlers": [
            "console"
        ],

        "level": "INFO",
    },
}


# =========================================================
# END OF SETTINGS
# =========================================================