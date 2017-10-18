# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
#print(dataset)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building an optimal Model using Backward Elimination
import statsmodels.formula.api as sm

'''Adding a column of ones to the dataset as it is required by the library statsmodels as the multiLinear eq. has a constant w/o an independent var, if no such column is provided then 1 variable would be ignored leading to an incorrect model.''' 

#X = np.append(arr = X, values = np.ones((50, 1)), axis = 1) >>This adds the column of ones to the dataset but as the last column.
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1) # Adds the column of ones as first column.

#================ Below this point is iterative and continues until the best fit model======================#
# Significance Level(SL) = 0.05
X_opt = X[:, [0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
#print(regressor_OLS.summary())

X_opt = X[:, [0,1,3,4,5]]                              # removed 2 as the p value was highest and greater than SL.
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()  # Model has to be refitted everytime a cloumn in removed.
#print(regressor_OLS.summary())

X_opt = X[:, [0,3,4,5]]                                # removed 1 as the p value was highest and greater than SL.
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())

X_opt = X[:, [0,3,5]]                                  # removed 1 as the p value was highest and greater than SL.
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())
