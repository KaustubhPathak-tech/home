"""
WSGI config for home project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

try:
    application = get_wsgi_application()
    app = application        # required for Vercel
except Exception as e:
    print("WSGI Import Failed", file=sys.stderr)
    import traceback
    traceback.print_exc()
    raise e


# application = get_wsgi_application()

# app=application  # for 'vercel' deployment
