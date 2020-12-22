# -*- coding: utf-8 -*-
"""Assignment7b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YVm0RLoQBOmnIFx1M0gY_vm9DVd7S-mP
"""

import pandas as pd
data=pd.read_excel("Load Data.xlsx")
data.shape

day_1 = data.iloc[0:-24, 2]
day_2 = data.iloc[24:, 2]
print(day_1.shape)
print(day_2.shape)

#The index of day_2 series starts from 24, so resetting the index
day_2 = day_2.reset_index()
day_2 = day_2['Load (kW)']

df = pd.concat([day_1, day_2], axis = 1)
df.shape

df.columns = ['Day_1', 'Day_2']
df.head

normalized_df = (df-df.mean())/df.std()
normalized_df.head()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(normalized_df.Day_1, normalized_df.Day_2, test_size = 0.10, random_state = 42)

m = 1 #Initial value of slope
c = -1 #Initial value of intercept
lr = 0.01 #Learning Rate
delta_m = 1 #Initialising Δm
delta_c = 1 #Initialising Δc
v_m = 0
v_c = 0
lam = 0.9
max_iters = 100 #Maximum number of iterations  
iters_count = 0 #Counting Iterations


def deriv(m_f, c_f, x, y):
  m_deriv = -1*(y-m_f*x-c_f)*x
  c_deriv = -1*(y-m_f*x-c_f)
  return m_deriv, c_deriv  


while iters_count < max_iters:
  for i in range(x_train.shape[0]):
    delta_m, delta_c = deriv(m, c, x_train.iloc[i], y_train.iloc[i])
    v_m = lam * v_m - lr * delta_m
    v_c = lam * v_c - lr * delta_c
    m += v_m
    c += v_c
  iters_count += 1
  print(f"Iteration: {iters_count}\tValue of m: {m}, \tValue of c: {c}")
print(f"\nThe local minima occurs at: {m}, {c}")

import numpy as np

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

y_pred_train = []
for i in x_train:
  y_p_tr = (m * i) + c
  y_pred_train.append(y_p_tr)
y_pred_train = np.array(y_pred_train)

y_pred_test = []
for i in x_test:
  y_p_te = (m * i) + c
  y_pred_test.append(y_p_te)
y_pred_test = np.array(y_pred_test)

import math
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error

#Training Accuracies
mse = math.sqrt(mean_squared_error(y_train, y_pred_train)) 
print('Root mean square error', mse) 
mse = (mean_squared_error(y_train, y_pred_train)) 
print('Mean square error', mse) 
mae=mean_absolute_error(y_train, y_pred_train)
print('Mean absolute error', mae)

mse = math.sqrt(mean_squared_error(y_test, y_pred_test)) 
print('Root mean square error', mse) 
mse = (mean_squared_error(y_test, y_pred_test)) 
print('Mean square error', mse) 
mae=mean_absolute_error(y_test, y_pred_test)
print('Mean absolute error', mae)

hour = input()
index = 2137 + int(hour)
x = normalized_df.iloc[index, 1]
normalised_output = m * x + c
output = (normalised_output * df.std()) + df.mean()
print(f"Predicted Load (kW) at {hour} hours on 1st December, 2018: {output[0]}")