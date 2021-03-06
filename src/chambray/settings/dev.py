from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DEV_SECRET_KEY', None)


# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass

GOOGLE_RECAPTCHA_SITE_KEY = '6Le9waAUAAAAAG7MVVF9r6GMVltJp88egk8An1pF'
GOOGLE_RECAPTCHA_SECRET_KEY = '6Le9waAUAAAAANyXrlCEohvlQJ9hnr45ORUI3iZ8'
