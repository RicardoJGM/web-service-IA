import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Data Collection and Pre Processing
# 1 Load Data from csv file to a pandas datafram
raw_mail_data = pd.read_csv('Identify-Spam-Email-ML-Model/mail_data.csv')
mail_data = raw_mail_data.where(pd.notnull(raw_mail_data),'')

#  Label Encoding
mail_data.loc[mail_data['Category'] == 'spam', 'Category'] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category'] = 1

X = mail_data['Message']
Y = mail_data['Category']

X_Train,X_test,Y_Train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=3)

# Feature Extraction 
# Transform text data to feature vectors that can be used as input to the logistic regression
feature_extraction = TfidfVectorizer(min_df=1,stop_words='english',lowercase=True)

X_train_feature = feature_extraction.fit_transform(X_Train)
X_test_feature = feature_extraction.transform(X_test)

#  Convert Y_train and Y_test as Integers
Y_Train = Y_Train.astype('int')
Y_test = Y_test.astype('int')

# Training the Model
# Logistic Regression
model = LogisticRegression()

model.fit(X_train_feature,Y_Train)

# Evaluating the Trained Model
# Predition on Training Model
prediction_on_Training_Data = model.predict(X_train_feature)
accuracy_on_training_data = accuracy_score(Y_Train,prediction_on_Training_Data)

print("Accuracy for Training : ",accuracy_on_training_data * 100)

# Predict on Test Data
prediction_on_Test_Data = model.predict(X_test_feature)
accuracy_on_test_data = accuracy_score(Y_test,prediction_on_Test_Data)

print("Accuracy for Training : ",accuracy_on_test_data * 100)

predictions = model.predict(X_test_feature)
# print(classification_report(Y_test, predictions),'\n')
# print(confusion_matrix(Y_test, predictions))

#  Building a Predictable System
input_mail = ["Dear friend, I am a Financial Consultant in control of privately owned funds placed for long term investments. My client intends to invest these funds in projects. I am willing to finance projects at a guaranteed 5% ROI per annum for projects ranging from 2 years term and above but not exceeding 12 years. Please answer ASAP."]

# Convert Text to feature vectors
input_data_feature = feature_extraction.transform(input_mail)

# Making Prediction
prediction = model.predict(input_data_feature)

print(prediction)

if(prediction == [1]):
    print("This is the Ham Mail.")
else:
    print("This is the Spam Mail.")
