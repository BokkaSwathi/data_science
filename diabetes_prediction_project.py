# -*- coding: utf-8 -*-
"""Diabetes_Prediction_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_fqvANnqb6thbTv8bl-WZHlgBBI_QEZU
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

df = pd.read_csv('/content/drive/MyDrive/diabetes.csv')

from google.colab import drive
drive.mount('/content/drive')

df.head()

df.shape

df.describe()

df['Outcome'].value_counts()

"""# 0 - non diabetic
# 1 - diabetic
"""

X = df.drop(columns='Outcome',axis=1)
y = df['Outcome']

X

y

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

standardized_data

X = standardized_data

X

y

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

X_train.shape

X_test.shape

"""# Train the model"""

clf = svm.SVC(kernel='linear')

clf.fit(X_train,y_train)

X_train_prediction = clf.predict(X_train)
accuracy_score(X_train_prediction,y_train)

"""# Accuracy on test data"""

X_test_prediction = clf.predict(X_test)
accuracy_score(X_test_prediction,y_test)

input_sample = (5,166,72,19,175,22.7,0.6,51)

input_np_array = np.asarray(input_sample)

input_np_array_reshaped = input_np_array.reshape(1,-1)

std_data = scaler.transform(input_np_array_reshaped)

std_data

prediction = clf.predict(std_data)

prediction

if (prediction[0]==0):
    print("Person is not diabetic")
else:
    print("Person is diabetic")