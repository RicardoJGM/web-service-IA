#Created by:
# - Ricardo de Jesús García Mejía - 200820130@ucc.mx
# - José Adolfo Jiménez Solís - 202060215@ucc.mx
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
import io

# Cargar los datos
df = pd.read_csv('spam.csv')

# Visualización de la distribución de las categorías
plt.figure(figsize=(8, 8))
df['Category'].value_counts().plot(kind='pie', autopct='%1.0f%%')
plt.title('Distribución de categorías')
plt.savefig('Images/Grafico de Distribucion de categorías')

# Separar los datos en características (X) y etiquetas (y)
x = df['Message'].values
y = df['Category'].values

# Dividir los datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Vectorizar el texto
cv = CountVectorizer()
x_train = cv.fit_transform(x_train)
x_test = cv.transform(x_test)

# Entrenar el modelo SVC
model = SVC(random_state=0, probability=True)
model.fit(x_train, y_train)

# Evaluar la precisión del modelo
score = model.score(x_test, y_test)
print(f"Accuracy: {score}")

# Generar predicciones
y_pred = model.predict(x_test)

# Matriz de Confusión
mc = confusion_matrix(y_test, y_pred)
etiquetas = sorted(list(set(y_test)))

fig, ax = plt.subplots(figsize=(10, 7))
sns.heatmap(mc, annot=True, fmt='d', cmap='Blues', xticklabels=etiquetas, yticklabels=etiquetas, ax=ax)
ax.set_xlabel('Predicted')
ax.set_ylabel('True')
ax.set_title('Matriz de confusión')

# Guardar la imagen de la matriz de confusión
fig.savefig('Images/Matriz de confusion.png')

# Reporte de Clasificación
reporte = classification_report(y_test, y_pred)

# Guardar el reporte de clasificación en un archivo de texto
with open('Reporte de clasificacion.txt', 'w') as f:
    f.write(reporte)

# Función para predecir si un mensaje es Spam o Ham y la probabilidad de ser Spam
def classify_message(message):
    message_transformed = cv.transform([message])
    prediction = model.predict(message_transformed)
    probability = model.predict_proba(message_transformed)
    spam_probability = probability[0][1] * 100
    return prediction[0], spam_probability

# Función para predecir y devolver resultados como cadena
def predict_mail_body(mailbody):
    if not mailbody:
        return "The Given Message is Empty"
    
    classification, spam_probability = classify_message(mailbody)
    return f"The Evaluated Message is classified as: {classification}\nProbability to be Spam: {spam_probability:.2f}%"
