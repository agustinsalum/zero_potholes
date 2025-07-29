
"""
Configurar la interfaz ASGI (Asynchronous Server Gateway Interface)

Servidor Asincrónico para WebSockets, tareas en tiempo real. Servidores como Uvicorn, Daphne, Hypercorn
"""

import os
from django.core.asgi import get_asgi_application

# Archivo de configuracion
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zero_potholes.settings')
# Instancia de la aplicación que puede ser utilizada por servidores ASGI
application = get_asgi_application()
