# Zero Potholes - Backend

Este proyecto corresponde a la parte **backend** de la aplicación **Zero Potholes**, desarrollado con **Django** y **Django REST Framework (DRF)**.  
Provee una API para gestionar reportes de baches, usuarios, ciudades, provincias y moderadores.

---

## 🚀 Puesta en marcha

### 1. Crear y activar entorno virtual (recomendado)

- En la raíz del proyecto:
    ```bash
    python -m venv venv

- Activar el entorno:
    ```bash
    source venv/bin/activate
    
### 2. Instalar dependencias

- Instalamos las dependencias necesarias:
    ```bash
    pip install -r requirements.txt

### 3. Migrar la base de datos

- Aplicamos las migraciones a la base de datos:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

### 4. Crear un superusuario (para acceder a /admin)

- Creamos al superusuario:
    ```bash
    python manage.py createsuperuser

### 5. Levantar el servidor de desarrollo

- Iniciamos el servidor con:
    ```bash
    python manage.py runserver

## Tecnologías utilizadas

- Django

- Django REST Framework (DRF)

- PostgreSQL

- Pillow
