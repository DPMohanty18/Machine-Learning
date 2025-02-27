import numpy as np
import pandas as pd

data=pd.read_csv(r"C:\Data\tabularData\normal_data\heart.csv")
print(data.head())

from sklearn.model_selection import train_test_split
target=data["target"]
features=data.drop("target",axis=1)
x_train,x_test,y_train,y_test=train_test_split(features,target,test_size=0.25)

from sklearn.ensemble import  RandomForestClassifier
model=RandomForestClassifier()
model.fit(x_train,y_train)
pred=model.predict(x_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,pred))

## model save 

import joblib

# Save the model to a file
#joblib.dump(model, 'random_forest_model.joblib')

import joblib

# Load the model from the file
loaded_model = joblib.load('random_forest_model.joblib')

# Use the loaded model to make predictions
predictions = loaded_model.predict(x_test)
print(predictions)
