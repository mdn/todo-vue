from pathlib import Path
from environs import Env


# Variables
# =======================================================================
env = Env()


# Constants
# =======================================================================
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', True)
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Allowed hosts
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]


# CSRF Trusted origin
# ------------------------------------------------------------------------------
CSRF_TRUSTED_ORIGINS = [
    'http://localhost',
    'http://127.0.0.1',
]


# CORS Origin whitelist
# ------------------------------------------------------------------------------
CORS_ORIGIN_WHITELIST = (
    # vue development server
    'http://localhost:8080',
    'http://127.0.0.1:8080',
)


# Application definition
# =======================================================================
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'corsheaders',
    'debug_toolbar',
]

LOCAL_APPS = [
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# Middlewares
# =======================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]


# Templates
# =======================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# Database
# =======================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# =======================================================================
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
# =======================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# =======================================================================
STATIC_URL = 'static/'


# SSL security
# ------------------------------------------------------------------------------
# SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', False)


# HSHS
# ------------------------------------------------------------------------------
SECURE_HSTS_SECONDS = env.int('DJANGO_SECURE_HSTS_SECONDS', 0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    'DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', False)
SECURE_HSTS_PRELOAD = env.bool('DJANGO_SECURE_HSTS_PRELOAD', False)


# Secure coockies
# ------------------------------------------------------------------------------
# SESSION_COOKIE_SECURE = env.bool('DJANGO_SESSION_COOCKIE_SECURE', False)
# CSRF_COOKIE_SECURE = env.bool('DJANGO_CSRF_COOCKIE_SECURE', False)


# Email config
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# REST Framework config
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}


# Django debug toolbar config
# ------------------------------------------------------------------------------
if DEBUG:
    import socket
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind('.')] + '.1' for ip in ips] + \
        ['127.0.0.1', '10.0.2.2']
