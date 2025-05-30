import os
# import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'iacxn5akgsn'

DEBUG = bool(os.environ.get('DEBUG', True))
DEBUG = True
# Because test settings will trigger KEEN.io hits
KEEN_DEBUG = bool(os.environ.get('DEBUG', True))
KEEN_DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

CUSTOM_APPS = (
    'resources',
    'rest_framework',
    'markdown_deux',
    'corsheaders',
    'clear_cache',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
) + CUSTOM_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'swapi.urls'

WSGI_APPLICATION = 'swapi.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_ETAGS = True
USE_I18N = True
USE_L10N = True
USE_TZ = True

#Removed - Chuck

# if not DEBUG:
#     DATABASES['default'] =  dj_database_url.config()
#     DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Do not use this with CloudFlare - instead force it below
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_PROXY_SSL_HEADER = ('CloudFlare_is_weird', None)

# Somehow with Cloudflare and PythonAnywhere - this does not work
# https://security.stackexchange.com/questions/8964/trying-to-make-a-django-based-site-use-https-only-not-sure-if-its-secure
# os.environ['HTTPS'] = "on"
# os.environ['wsgi.url_scheme'] = 'https'

# So I hacked the _get_scheme code - look for CHUCK HACK
# /home/dj4e/.virtualenvs/django1/lib/python2.7/site-packages/django/http/request.py
# /home/dj4e/.virtualenvs/django1/lib/python2.7/site-packages/django/core/handlers/wsgi.py
#
# def _get_scheme(self):
#     return 'https'
#

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Removed by Chuck
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'TIMEOUT': 60
#     }
# }

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# Markdown

MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": False,
    },
}

# REST Framework

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'resources.renderers.WookieeRenderer'
    ),
    'PAGINATE_BY': 10,
## Removed by Chuck 8-Dec-23
##    'DEFAULT_THROTTLE_CLASSES': (
##        'rest_framework.throttling.AnonRateThrottle',
##    ),
##    'DEFAULT_THROTTLE_RATES': {
##        'anon': '10000/day',
##    },
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
    )
}

# Keen.io

KEEN_PROJECT_ID = os.environ.get('KEEN_PROJECT_ID', '')
KEEN_WRITE_KEY = os.environ.get('KEEN_WRITE_KEY', '')
KEEN_READ_KEY = os.environ.get('KEEN_READ_KEY', '')
KEEN_CELERY = False

# Stripe

STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY', '')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY', '')
STRIPE_TEST_PUBLISHABLE_KEY = os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY', '')

if DEBUG:
    STRIPE_KEYS = {
        "secret" :STRIPE_TEST_SECRET_KEY,
        "publishable": STRIPE_TEST_PUBLISHABLE_KEY
    }
else:
    STRIPE_KEYS = {
        "secret" :STRIPE_SECRET_KEY,
        "publishable": STRIPE_PUBLISHABLE_KEY
    }

# Cors

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_METHODS = (
        'GET',
    )

# Removed by Chuck
# Memcache
#from memcacheify import memcacheify
# CACHES = memcacheify()


APPEND_SLASH = True

# Needed for 3.2 and later
# https://stackoverflow.com/questions/67783120/warning-auto-created-primary-key-used-when-not-defining-a-primary-key-type-by
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

