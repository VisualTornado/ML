#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:12:04 2019

@author: akshayawasthy
"""
# TOEFL GRE, CGPA

import numpy as np
import pandas as pd
import matplotlib as plt

rawdata = pd.read_csv("/Users/akshayawasthy/Downloads/Predict_Addmission.csv")
data = rawdata.iloc[:,[1,2,3,4,5,6,7,8]] #1-GRE, 6-CGPA, 4-SOP

X = data.iloc[:,[0,1,2,3,4,5,6]]
y = data.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = .20, random_state = 0)

data.corr()

from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns

vif.round(1)

import statsmodels.formula.api as sm

X = np.append(arr = np.ones((500,1)).astype(int), values = X,axis=1)

X_new = X_train[:,[0,1,2,3,4,5,6,7]] #4
regressor = sm.OLS(endog = y, exog = X_new).fit()

regressor.summary()

y_pred_OLS = regressor.predict(X_new)

np.sum(np.abs(y - y_pred_OLS))/np.sum(y)

"""
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train,y_train)
reg.score(X_train,y_train)

ypred_train = reg.predict(X_train)
y_pred_test = reg.predict(X_test)

np.sum(np.abs(y_test - y_pred_test))/np.sum(y_test)

"""