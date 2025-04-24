"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
>>>>>>> bad32a02db6e9749226952f34a9a6794817cfe25
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
>>>>>>> bad32a02db6e9749226952f34a9a6794817cfe25

application = get_asgi_application()
