# -*- coding: utf-8 -*-
"""Assignment_5B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15zznpqOkt9wSXuoL1V9VPNqiTopR0xRG
"""

import pandas as pd
import numpy as np
data=pd.read_csv('assignment_5.csv')

from sklearn import preprocessing
data= preprocessing.normalize(data)

data= pd.DataFrame(data=data, columns=["X", "Y"])
data

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data.X, data.Y, test_size = 0.10, random_state = 4)

m = 1 #Initial value of slope
c = -1 #Initial value of intercept
lr = 0.01 #Learning Rate
delta_m = 1 #Initialising Δm
delta_c = 1 #Initialising Δc
max_iters = 1000 #Maximum number of iterations  
iters_count = 0 #Counting Iterations

def deriv(m_f, c_f, datax, datay):
    m_deriv = 0
    c_deriv = 0
    for i in range(datax.shape[0]):
        x, y = datax.iloc[i], datay.iloc[i]
        m_deriv += (y-m_f*x-c_f)*x
        c_deriv += (y-m_f*x-c_f)
        m_deriv = -m_deriv/len(datax)
        c_deriv = -c_deriv/len(datay)
    return m_deriv, c_deriv  


while iters_count < max_iters:
    delta_m, delta_c = deriv(m, c, x_train, y_train)
    delta_m = -lr * delta_m
    delta_c = -lr * delta_c
    m += delta_m
    c += delta_c
    iters_count += 1
    print(f"Iteration: {iters_count}\tValue of m: {m}, \tValue of c: {c}")

print(f"\nThe local minima occurs at: {m}, {c}")

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

i=0
y_pred=[]
while i<27:
    y_predict=(m*x_train[i])-c
    y_pred.append(y_predict)
    i=i+1

i=0
yt_pred=[]
while i<3:
    yt_predict=(m*x_test[i])-c
    yt_pred.append(yt_predict)
    i=i+1

import math
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error


def accuracy_op(y_train,y_pred):
    mse = math.sqrt(mean_squared_error(y_train,y_pred)) 
    print('Root mean square error', mse) 
    mse = (mean_squared_error(y_train,y_pred)) 
    print('Mean square error', mse) 
    mae=mean_absolute_error(y_train, y_pred)
    print('Mean absolute error', mae)

print(accuracy_op(y_train,y_pred))

print(accuracy_op(y_test,yt_pred))

