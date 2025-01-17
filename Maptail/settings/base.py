"""
Django settings for Maptail project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from pygeoapi.models.config import APIRules
from pygeoapi.config import get_config
from pygeoapi.openapi import load_openapi_document
from pygeoapi.util import get_api_rules
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent.parent

dotenv_path = os.path.join(str(BASE_DIR), '.env')
load_dotenv(dotenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    # This project
    "website",
    "custom_media",
    "custom_user",
    # Wagtail CRX (CodeRed Extensions)
    "coderedcms",
    "django_bootstrap5",
    "modelcluster",
    "taggit",
    "wagtailcache",
    "wagtailseo",
    # Wagtail
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail",
    "wagtail.contrib.settings",
    "wagtail.contrib.table_block",
    "wagtail.admin",
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.gis",

    # Maptail
    "base",
    "features",
    "resources",
    "resource_attributes",
    "resource_files",
    "metadata",

    # Third-party
    "rest_framework",
    "rest_framework_gis",
    "django_json_widget",
    "polymorphic",
    "wagtail_rangefilter",
    "rangefilter",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.openid_connect",
    'pygeoapi',
]

MIDDLEWARE = [
    # Save pages to cache. Must be FIRST.
    "wagtailcache.cache.UpdateCacheMiddleware",
    # Common functionality
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.CommonMiddleware",
    # Security
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # CMS functionality
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    # AllAuth
    "allauth.account.middleware.AccountMiddleware",
    # Fetch from cache. Must be LAST.
    "wagtailcache.cache.FetchFromCacheMiddleware",

    # pygeoapi
    "resources.middleware.DynamicPygeoapiConfigMiddleware",
]

ROOT_URLCONF = "Maptail.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "Maptail.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
        "NAME": BASE_DIR / "db.spatialite",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "custom_user.User"

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# Login

LOGIN_URL = "wagtailadmin_login"
LOGIN_REDIRECT_URL = "wagtailadmin_home"

# Wagtail settings

WAGTAIL_SITE_NAME = "Maptail"

WAGTAIL_ENABLE_UPDATE_CHECK = False

WAGTAILIMAGES_IMAGE_MODEL = "custom_media.CustomImage"

WAGTAILDOCS_DOCUMENT_MODEL = "custom_media.CustomDocument"

WAGTAILIMAGES_EXTENSIONS = ["gif", "jpg", "jpeg", "png", "webp", "svg"]

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://maptail.maptitud.xyz"

# Tags

TAGGIT_CASE_INSENSITIVE = True

# Sets default for primary key IDs
# See https://docs.djangoproject.com/en/5.0/ref/models/fields/#bigautofield
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Disable built-in CRX Navbar and Footer since this project has a
# custom implementation.
CRX_DISABLE_NAVBAR = True
CRX_DISABLE_FOOTER = True

# Maptail settings

USE_AUDITLOG = False

if USE_AUDITLOG:
    INSTALLED_APPS.append("auditlog")
    MIDDLEWARE.append("auditlog.middleware.AuditlogMiddleware")
    AUDITLOG_INCLUDE_ALL_MODELS = True

OL_MAP_ZOOM = 11
OL_MAP_CENTER = [-101.2, 24.8]
OL_MAP_CENTER_LON = -101.2
OL_MAP_CENTER_LAT = 24.8

ENABLE_MAP_CENTER_FROM_USER_LOCATION = True
ENABLE_MODELS_REVISIONS = True

DATA_FEATURES_SRID = 4326
USE_RICHTEXT_TEXTFIELD = True

# pygeoapi settings
PYGEOAPI_CONFIG = get_config()
OPENAPI_DOCUMENT = load_openapi_document()
API_RULES = get_api_rules(PYGEOAPI_CONFIG)

# print("PYGEOAPI_CONFIG", PYGEOAPI_CONFIG)
# print("OPENAPI_DOCUMENT", OPENAPI_DOCUMENT)

# Defaults to True in Django
# https://docs.djangoproject.com/en/3.2/ref/settings/#append-slash
APPEND_SLASH = not API_RULES.strict_slashes

# print("APPEND_SLASH", APPEND_SLASH)
# print("PI_RULES.strict_slashes", API_RULES.strict_slashes)


# Custom

DATA_UPLOAD_MAX_MEMORY_SIZE = None
