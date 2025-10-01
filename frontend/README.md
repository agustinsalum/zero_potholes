# Zero Potholes - Frontend

Este proyecto utiliza **React** con **Vite** para la parte frontend de la aplicación.

---

## 🚀 Puesta en marcha

Para levantar el servidor de desarrollo:

1. Abrir una terminal en la carpeta raíz del proyecto.  

2. Ir a la carpeta del frontend:
   ```bash
   cd frontend

3. Instalar las dependencias necesarias:
    ```bash
    npm install

4. Iniciar el servidor de desarrollo:
    ```bash
    npm run dev

5. Abrir en el navegador el enlace que muestra la terminal (por defecto suele ser http://localhost:5173/).

## Instalar Node.js y npm usando Node Version Manager (NVM)

> Recomendado para mantener múltiples versiones de Node.js en tu sistema.

1. Descargar e instalar NVM:
   ```bash
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

> Si no tienes curl, instálalo previamente con tu gestor de paquetes (apt, brew, etc.).

2. Reiniciar la terminal o ejecutar:
    ```bash
    source ~/.bashrc

3. Verificar la instalación de NVM:
    ```bash
    nvm -v

4. Listar todas las versiones disponibles de Node.js:
    ```bash
    nvm ls-remote

5. Instalar la última versión LTS recomendada:
    ```bash
    nvm install --lts

6. Usar esa versión en la sesión actual:
    ```bash
    nvm use --lts

7. Verificar que Node.js y npm están instalados correctamente:
    ```bash
    node -v
    npm -v

8. (Opcional) Establecer una versión como predeterminada:
    ```bash
    nvm alias default <versión>

## 📜 Scripts útiles

Dentro de la carpeta `frontend` puedes usar:

- **Iniciar servidor de desarrollo**  
  ```bash
  npm run dev

- **Construir la aplicación para producción**
  ```bash
  npm run build

- **Previsualizar la build en local**
  ```bash
  npm run preview

- **Ejecutar linter para revisar el código**
  ```bash
  npm run lint

## Tecnologías utilizadas

- React
- Vite
- ESLint
- Bootstrap (a través de react-bootstrap)
- React Router DOM
