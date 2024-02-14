# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:02:38 2024

@author: rc_la
"""

import pandas as pd

dataset = pd.read_csv("C:/Users/rc_la/Downloads/Titanic.csv")

dataset.head()

import matplotlib.pyplot as plt

sex_counts = dataset.groupby('Sex')['Survived'].agg(['count', 'sum'])

plt.figure(figsize=(8, 6))

plt.bar(sex_counts.index, sex_counts['count'], label='Died')
plt.bar(sex_counts.index, sex_counts['sum'], label='Survived', alpha=0.7)

plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Total Count and Survivors by Sex')
plt.legend()

plt.show()

age_bins = [0, 18, 30, 40, 50, 60, 100]
age_labels = ['<18', '18-30', '30-40', '40-50', '50-60', '60+']

dataset['AgeGroup'] = pd.cut(dataset['Age'], bins=age_bins, labels=age_labels)

age_group_data = dataset.groupby('AgeGroup')['Survived'].agg(['count', 'sum'])
age_group_data['SurvivalRate'] = (age_group_data['sum'] / age_group_data['count']) * 100

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(age_group_data.index, age_group_data['count'], color='skyblue', label='Total Passengers')

ax1.set_xlabel('Age Group')
ax1.set_ylabel('Total Passengers', color='skyblue')
ax1.set_title('Total Passengers and Survival Rate by Age Group')

ax2 = ax1.twinx()
ax2.plot(age_group_data.index, age_group_data['SurvivalRate'], marker='o', color='green', label='Survival Rate (%)')

ax2.set_ylabel('Survival Rate (%)', color='green')

plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
        
      
 