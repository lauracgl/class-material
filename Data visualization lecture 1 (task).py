# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:57:13 2024

@author: rc_la
"""

import pandas as pd

dataset = pd.read_csv('C:/Users/rc_la/Downloads/mtcars (1).csv')

dataset.head()

grouped_data = dataset['cyl'].value_counts()

import matplotlib.pyplot as plt

plt.bar(grouped_data.index, grouped_data.values, color='blue')

plt.title('Number of Vehicles by Cylinder')
plt.xlabel('Cylinders')
plt.ylabel('Count')

plt.show()

import seaborn as sns

sns.regplot(x=dataset['hp'], y=dataset['qsec'])

plt.title('Effect of Horsepower on 1/4 Completion time')
plt.xlabel('Horsepower')
plt.ylabel('1/4 mile in seconds')

plt.show()

import statsmodels.api as sm

x_with_intercept = sm.add_constant(dataset['hp'])
model = sm.OLS(dataset['qsec'], x_with_intercept)
result = model.fit()
slope = result.params[1]
intercept = result.params[0]
r_squared = result.rsquared

sns.regplot(x=dataset['hp'], y=dataset['qsec'])

equation = f'y = {intercept:.2f} + {slope:.2f}x'
r_squared_text = f'R-squared = {r_squared:.2f}'
plt.text(0.5, 9, equation, ha='center')
plt.text(0.5, 10, r_squared_text, ha='center')

plt.title('Effect of Horsepower on 1/4 Completion time')
plt.xlabel('Horsepower')
plt.ylabel('1/4 mile in seconds')

plt.show()