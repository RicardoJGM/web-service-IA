import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Cargar los datos
df = pd.read_csv('spam.csv')

#df.info()
#print(df.shape)
#print(df.head())

# Visualización de la distribución de las categorías
# plt.figure(figsize=(8, 8))
# df['Category'].value_counts().plot(kind='pie', autopct='%1.0f%%')
# plt.title('Pie chart')
# plt.show()

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

# Función para predecir si un mensaje es Spam o Ham y la probabilidad de ser Spam
def classify_message(message):
    message_transformed = cv.transform([message])
    prediction = model.predict(message_transformed)
    probability = model.predict_proba(message_transformed)
    spam_probability = probability[0][1] * 100
    return prediction[0], spam_probability

# Solicitar un mensaje al usuario y clasificarlo
# user_message = input("Ingrese el mensaje a clasificar: ")
def predict_mail_body(mailbody):
    classification, spam_probability = classify_message(mailbody)
    return(f"El mensaje introducido es clasificado como: {classification}\nProbabilidad de ser Spam: {spam_probability:.2f}%")