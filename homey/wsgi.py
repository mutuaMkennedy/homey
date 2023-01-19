import os
from .settings import base
from django.core.wsgi import get_wsgi_application

 #change this to match environment

application = get_wsgi_application()

if base.DEBUG==False:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homey.settings.prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homey.settings.local')

application = get_wsgi_application()