import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Data Collection and Pre Processing
# 1 Load Data from csv file to a pandas datafram
raw_mail_data = pd.read_csv('Identify-Spam-Email-ML-Model/mail_data.csv')
print(raw_mail_data.head())