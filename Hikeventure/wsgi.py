"""
WSGI config for Hikeventure project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hikeventure.settings')
# manual
os.environ['DJANGO_SETTINGS_MODULE'] = 'Hikeventure.settings' 
# settings.configure()
application = get_wsgi_application()
