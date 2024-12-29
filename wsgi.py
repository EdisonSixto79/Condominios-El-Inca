import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'condominios_el_inca.settings')  # Cambia 'condominios_el_inca' por el nombre de tu carpeta del proyecto si es diferente

application = get_wsgi_application()

