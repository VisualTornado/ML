# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting the Model to train 
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train) # Fit the model to your training data.

# Predicting Independent on test data

y_pred = regressor.predict(X_test)                              # The independent set prediction can be compared to the y_test data set to check how fit is the model.

# Visualizing the training set results

plt.scatter (X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')  
plt.label('Salary vs Experiance Training')
plt.xlabel('Experiance')
plt.ylabel('Salary')
plt.show()

# Visualizing the test set results

plt.scatter (X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')   # We keep the same regression line as the model has been trained on the data set so even if you change to test the line shall be same.
plt.label('Salary vs Experiance Training')
plt.xlabel('Experiance')
plt.ylabel('Salary')
plt.show()

NOTE: Visualizing helps understand how good the regression model fits the data set.
