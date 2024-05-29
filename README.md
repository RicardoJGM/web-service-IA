# Identificación de Correos Spam
## Objetivo del Script
El objetivo de este script es desarrollar un modelo de Machine Learning para identificar correos spam utilizando técnicas de procesamiento de texto y aprendizaje supervisado. Además, se crea una interfaz web con Flask para facilitar la interacción con el modelo.

## En qué Consiste
Se trata de un projecto final en el cual se encuentran 2 scripts de python: 
- app.py: el cual se encarga de proporcionar un servicio por medio de webservice de una página web que tiene como objetivo recibir un mensaje de cuerpo de email en inglés para procesarlo y determinar si se trata de spam o no.
- preprocessing.py: este script contiene el modelo SVM con el que se entrenó con un set de datos de correos spam y no spam, además contiene la generación de métricas y el porcentaje de predicción efectiva del modelo, cuenta con una función la cual se le proporciona a app.py para delimitar si el texto enviado es spam o no. 
### Librerías Utilizadas
- Flask: Utilizado para crear la interfaz web.
- Pandas y NumPy: Para la manipulación y análisis de datos.
- Scikit-Learn: Para la construcción del modelo de Machine Learning.
- Seaborn: Proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos y con estilo.
- Otros paquetes como Joblib, Jinja2, y Werkzeug para funcionalidades adicionales en servicios web.

### Modelos Utilizados
SVM (Support Vector Machines): es un algoritmo de aprendizaje supervisado que se utiliza en muchos problemas de clasificación y regresión, incluidas aplicaciones médicas de procesamiento de señales, procesamiento del lenguaje natural y reconocimiento de imágenes y voz.

El objetivo del algoritmo SVM es encontrar un hiperplano que separe de la mejor forma posible dos clases diferentes de puntos de datos. “De la mejor forma posible” implica el hiperplano con el margen más amplio entre las dos clases, representado por los signos más y menos en la siguiente figura. El margen se define como la anchura máxima de la región paralela al hiperplano que no tiene puntos de datos interiores. El algoritmo solo puede encontrar este hiperplano en problemas que permiten separación lineal; en la mayoría de los problemas prácticos, el algoritmo maximiza el margen flexible permitiendo un pequeño número de clasificaciones erróneas.

![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/73cce429-ad41-43d9-8201-4c29099bcc2e)                                                                                                                                                       
                                                  *Definición del “margen” entre clases: el criterio que los SVM intentan optimizar.*

Puntos clave:
- Support vector machines son muy populares y logran un buen rendimiento en muchas tareas de clasificación y regresión.
- Aunque los algoritmos SVM están formulados para la clasificación binaria, los algoritmos SVM multiclase se construyen combinando varios clasificadores binarios.
- Los kernels hacen que los SVM sean más flexibles y capaces de gestionar problemas no lineales.
- Para construir la superficie de decisión, solo se requieren los vectores de soporte seleccionados a partir de los datos de entrenamiento. Una vez terminado el entrenamiento, el resto de los datos de entrenamiento es irrelevante, produciendo una representación compacta del modelo que es adecuada para generar código de forma automatizada.

## Métricas obtenidas del modelo
### Gráfico de categorización del data frame
![Grafico de Distribucion de categorías](https://github.com/RicardoJGM/web-service-IA/assets/112904134/f9e39862-f183-4ba6-91fa-cce7763a30e8)

### Matriz de confusión del modelo
![Matriz de confusion](https://github.com/RicardoJGM/web-service-IA/assets/112904134/ece4df2c-310b-492f-be32-d4b2c95dafe4)

## Reporte de clasificación del modelo
| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| **ham**       | 0.98      | 1.00   | 0.99     | 955     |
| **spam**      | 0.99      | 0.88   | 0.93     | 160     |
| **accuracy**  |           |        | 0.98     | 1115    |
| **macro avg** | 0.99      | 0.94   | 0.96     | 1115    |
| **weighted avg** | 0.98   | 0.98   | 0.98     | 1115    |

## Integrantes y Roles en el Proyecto
* Jose Adolfo Jimenez Solis y  Ricardo de Jesus Garcia Mejia: Desarrolladores Backend.
* Carlos Santamaria Solina: Desarrollador Frontend.
* Diego Azpe Carmona: Analisis de Datos.

## Diagrama de Bloques

![diagrama de bloques](https://github.com/RicardoJGM/web-service-IA/assets/166866230/c619fba5-bdf1-4594-a7ef-17d6afc79140)

## Ejemplo de uso para preprocesamiento de datos y entrenamiento del modelo

![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/8c45b9e8-cbbd-45d8-b023-578cf7bd3a18)
![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/2ecbc425-9ab6-412b-ba6c-e9a31a5c2d6b)
![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/336d7bb9-ace5-469e-b649-c4d45cd1db98)
![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/4129b8a8-1500-4bc5-a4d3-56b0fb30b875)
![image](https://github.com/RicardoJGM/web-service-IA/assets/166866230/d1a268f7-ced1-4480-ab0b-74824ae6dc00)

## Instalación
Para instalar las dependencias del proyecto, ejecuta el siguiente comando en tu entorno virtual:
`pip install -r requirements.txt`
