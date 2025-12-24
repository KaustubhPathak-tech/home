import os
from django.core.wsgi import get_wsgi_application
from vercel_wsgi import handle

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")  # change 'home' to your project name

application = get_wsgi_application()

def handler(request, response):
    return handle(request, response, application)
