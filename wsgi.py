import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'condominios_el_inca.settings')  # Ajusta 'condominios_el_inca' si es diferente

application = get_wsgi_application()

