from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('PROD_SECRET_KEY', None)
# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['.lordchambray.com', '.lordchambray.com.mt'] 
DEBUG = False

try:
    from .local import *
except ImportError:
    pass

WAGTAIL_CACHE = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# MAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST =  os.environ.get('SMTP_SERVER', None)
EMAIL_PORT = os.environ.get('SMTP_PORT', None)
EMAIL_HOST_USER = os.environ.get('SMTP_USER', None)
EMAIL_HOST_PASSWORD = os.environ.get('SMTP_PASSWORD', None)
DEFAULT_FROM_EMAIL = 'assist.tecne@gmail.com'

ADMINS = [
    ('Sergio Brero', 'sergio.brero.it@gmail.com'),
]
MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = '[LordChambray Wagtail] '
INTERNAL_IPS = ('127.0.0.1', '178.62.37.214')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

WAGTAIL_SITE_NAME = 'Lord Chambray Site'
BASE_URL = 'https://www.lordchambray.com.mt'

TAGGIT_CASE_INSENSITIVE = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter', 
    'compressor.filters.cssmin.rCSSMinFilter'
]
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

COMPRESS_OUTPUT_DIR = 'compressed'
GZIP_CONTENT_TYPES = (
    'text/css',
    'application/javascript',
    'application/x-javascript',
    'text/javascript'
)
HTML_MINIFY = True
COMPRESS_ENABLED = True
