"""
WSGI config for RoR project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os,sys
#from dj_static import Cling
from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/RunnerOnRoad')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ror.settings")

# application = Cling(get_wsgi_application())
application = get_wsgi_application()
