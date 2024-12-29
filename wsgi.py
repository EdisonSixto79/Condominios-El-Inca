import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'condominios_el_inca.settings')  # Reemplaza con el nombre de tu proyecto

application = get_wsgi_application()
