"""
WSGI config for chambray project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
from dotenv import load_dotenv
import os

from django.core.wsgi import get_wsgi_application

project_environ = '/var/virtual/chambray/bin'
load_dotenv(os.path.join(project_environ, '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chambray.settings.production")

application = get_wsgi_application()
