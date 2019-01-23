#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Book1.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 7].values

#Splitting the dataset into Training set and Testing set
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=100,random_state=0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)

#Predicting
y_pred = regressor.predict(X_test)