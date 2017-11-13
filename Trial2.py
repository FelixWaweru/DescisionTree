
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import preprocessing

# Reads the data from the data file
rawData = pd.read_csv('adult.data.txt',sep= ',', header= None)
print ("Dataset Lenght:: ", len(rawData))
print ("Dataset Shape:: ", rawData.shape)
# This converts the string variables into numerical values that an be manipulated by sklearn
rawData = rawData.apply(LabelEncoder().fit_transform)

# Predictor variables from the 1st to 14th column
X = rawData.values[:, 0:13]
# Outcome variables for the last column
# This will be used as the estimated outcome from the predictions
Y = rawData.values[:,14]
'''
This creates a training and test model
'test_size' stands for the size of the test model. ie; 30% test data, 70% training data.
'random_state' stands for the rate of random sampling from the data
'''
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 0)
'''
This creates a decision tree with information gain based analysis
'criterion' stands for the method that will be used to analyze the data
'random_state' stands for the rate of random sampling from the data
'''
treeData = DecisionTreeClassifier(criterion="entropy", random_state = 0)
# Place the data from the training models into the decision tree
treeData.fit(X_train, y_train)

y_pred_en = treeData.predict(X_test)
y_pred_en

print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)