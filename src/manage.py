#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv

project_environ = '/home/sergio/virtual/chambray/bin'

if __name__ == "__main__":
    # added to fix wrong pycharm .env files management
    load_dotenv(os.path.join(project_environ, '.env'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chambray.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
