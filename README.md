# Identificación de Correos Spam
## Objetivo del Script
El objetivo de este script es desarrollar un modelo de Machine Learning para identificar correos spam utilizando técnicas de procesamiento de texto y aprendizaje supervisado. Además, se crea una interfaz web con Flask para facilitar la interacción con el modelo.

## En qué Consiste
### Librerías Utilizadas
- Flask: Utilizado para crear la interfaz web.
- Pandas y NumPy: Para la manipulación y análisis de datos.
- Scikit-Learn: Para la construcción del modelo de Machine Learning.
- Otros paquetes como Joblib, Jinja2, y Werkzeug para funcionalidades adicionales.

## Modelos Utilizados
Logistic Regression: Modelo utilizado para la clasificación de correos como spam o no spam.

## Integrantes y Roles en el Proyecto
-Adolfo y  Ricardo: Desarrolladores Backend.
-Carlos: Desarrollador Frontend.
-Diego: Analisis de Datos.

## Diagrama de Bloques
El proceso de trabajo del proyecto se describe en el siguiente diagrama de bloques:
1. Carga de datos desde un archivo CSV.
2. Preprocesamiento de los datos (limpieza, codificación de etiquetas).
3. Extracción de características mediante TF-IDF Vectorizer.
4. División de datos en conjuntos de entrenamiento y prueba.
5. Entrenamiento del modelo Logistic Regression.
6. Evaluación del modelo y generación de métricas de rendimiento.
7. Creación de la interfaz web con Flask.
8. Despliegue del modelo y la interfaz en un entorno de producción.


## Ejemplo de uso para preprocesamiento de datos y entrenamiento del modelo

![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/8c45b9e8-cbbd-45d8-b023-578cf7bd3a18)
![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/2ecbc425-9ab6-412b-ba6c-e9a31a5c2d6b)
![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/336d7bb9-ace5-469e-b649-c4d45cd1db98)
![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/4129b8a8-1500-4bc5-a4d3-56b0fb30b875)
![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/d1a268f7-ced1-4480-ab0b-74824ae6dc00)

## Instalación
Para instalar las dependencias del proyecto, ejecuta el siguiente comando en tu entorno virtual:
`pip install -r requirements.txt`
