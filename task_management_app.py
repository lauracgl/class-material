#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install scikit-learn pandas numpy tensorflow keras flask


# In[12]:


CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    description TEXT,
    deadline DATE,
    estimated_duration INTEGER,
    priority INTEGER,
    actual_duration INTEGER,
    completion_status BOOLEAN
);

CREATE TABLE user_feedback (
    id INTEGER PRIMARY KEY,
    task_id INTEGER,
    user_feedback TEXT,
    FOREIGN KEY(task_id) REFERENCES tasks(id)
);


# In[ ]:


import tkinter as tk
from tkinter import ttk

class TimeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Management Application")
        self.create_widgets()
    
    def create_widgets(self):
        ttk.Label(self.root, text="Task Description").grid(column=0, row=0)
        self.task_desc = ttk.Entry(self.root)
        self.task_desc.grid(column=1, row=0)

        ttk.Label(self.root, text="Deadline").grid(column=0, row=1)
        self.deadline = ttk.Entry(self.root)
        self.deadline.grid(column=1, row=1)
        
        ttk.Label(self.root, text="Estimated Duration (minutes)").grid(column=0, row=2)
        self.estimated_duration = ttk.Entry(self.root)
        self.estimated_duration.grid(column=1, row=2)

        ttk.Label(self.root, text="Priority (1-5)").grid(column=0, row=3)
        self.priority = ttk.Entry(self.root)
        self.priority.grid(column=1, row=3)

        self.add_task_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(column=0, row=4, columnspan=2)

    def add_task(self):
        # Collect data and store in the database
        pass

root = tk.Tk()
app = TimeManagementApp(root)
root.mainloop()


# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# Load data
data = pd.read_csv("C:\Users\rc_la\Downloads\task_dataset.csv")

# Feature extraction and encoding
X = data[['deadline', 'estimated_duration', 'priority']]
y = data['actual_duration']
X = pd.get_dummies(X, columns=['priority'])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)


# In[ ]:


import joblib

# Save model
joblib.dump(model, 'task_completion_model.pkl')

# Load model in the application
model = joblib.load('task_completion_model.pkl')

def predict_task_duration(task):
    task_features = pd.DataFrame([task])
    task_features = pd.get_dummies(task_features, columns=['priority'])
    task_features = scaler.transform(task_features)
    predicted_duration = model.predict(task_features)
    return predicted_duration

