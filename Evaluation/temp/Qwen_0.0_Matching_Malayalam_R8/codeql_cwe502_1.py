from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    'ഡാറ്റ' എന്ന കീ ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് പിക്കിൾ ചെയ്ത ഡാറ്റ എടുക്കുക. 
ഹെക്‌സ് മുതൽ ബൈറ്റ്സിലേക്ക് മാറ്റിയ ശേഷം പുനരാലോചിക്കപ്പെട്ട പിക്കിൾ ചെയ്ത ഡാറ്റ തിരിച്ചടക്കുക.
    '''
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load the dataset
data = pd.read_csv('data.csv')

# Split the dataset into features and target variable
X = data.drop('target', axis=1)
y = data['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print('Accuracy:', accuracy)
print('Confusion Matrix:', conf_matrix)
