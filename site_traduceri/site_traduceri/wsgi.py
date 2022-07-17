"""
WSGI config for site_traduceri project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

site_traduceri = os.path.expanduser('-/site_traduceri')
load_dotenv(os.path.join(site_traduceri, '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_traduceri.settings')
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
