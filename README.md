# Spam Email Identifier

Este proyecto utiliza inteligencia artificial para identificar correos electrónicos de spam o malware. La aplicación está construida con Flask y varias otras librerías y paquetes de Python. La interfaz de usuario permite analizar el contenido de los correos electrónicos, y la comunicación entre el frontend y el backend se realiza mediante API.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción

El objetivo de este proyecto es implementar una interfaz de usuario que permita analizar el cuerpo de correos electrónicos para identificar si son spam o contienen malware. La aplicación utiliza un modelo de aprendizaje automático para clasificar los correos electrónicos y ofrece una API para la comunicación entre el frontend y el backend.

## Instalación

Para instalar y ejecutar este proyecto localmente, sigue los siguientes pasos:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/spam-email-identifier.git
    cd spam-email-identifier
    ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar el servidor Flask, usa el siguiente comando:
```bash
flask run
