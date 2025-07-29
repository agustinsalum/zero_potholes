
"""
Punto de entrada para desplegar tu proyecto Django en un servidor WSGI (Web Server Gateway Interface).

Servidor Sincrónico para HTTP tradicional. Servidores como 	Gunicorn, uWSGI, Apache + mod_wsgi
"""

import os
from django.core.wsgi import get_wsgi_application

# Archivo de configuracion
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zero_potholes.settings')
# Instancia que el servidor web va a usar para enviarle solicitudes a Django.
application = get_wsgi_application()
