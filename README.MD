# Zero Potholes — Backend

Backend de la plataforma **Zero Potholes**, desarrollado con **Django** y **Django REST Framework (DRF)**.  
Expone una API REST para gestionar denuncias ciudadanas sobre imperfecciones en la vía pública, incluyendo reportes, ubicaciones geográficas, estados, severidad y moderadores.

Este backend está diseñado para integrarse con un frontend web basado en mapas interactivos y autenticación de usuarios.

---

## Funcionalidades principales

- Registro de reportes con geolocalización
- Gestión de provincias y ciudades
- Estados y niveles de severidad configurables
- Asignación de reportes a moderadores
- Autenticación y panel administrativo
- Soporte para carga de imágenes

---

## Puesta en marcha

### 1. Crear y activar entorno virtual (recomendado)

Desde la raíz del proyecto:

```bash
python -m venv venv
```

Activar:

```bash
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

---

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 3. Crear archivo `.env` con credenciales

En el mismo nivel que `settings.py`:

```bash
touch .env
```

Ejemplo de contenido:

```env
SECRET_KEY=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
```

Podés generar una `SECRET_KEY` en: https://djecrety.ir/

---

### 4. Migrar la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Crear superusuario (para `/admin`)

```bash
python manage.py createsuperuser
```

---

### 6. Levantar servidor de desarrollo

```bash
python manage.py runserver
```

La API quedará disponible en:

```
http://127.0.0.1:8000/
```

Panel admin:

```
http://127.0.0.1:8000/admin/
```

---

## Tecnologías utilizadas

- Python 3
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Pillow
- python-dotenv

---

## Estructura general del proyecto

```bash
zero_potholes_backend/
├── apps/
├── config/
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

## Estado del proyecto

🟢 En desarrollo activo — arquitectura base completa, modelos definidos y API en expansión.