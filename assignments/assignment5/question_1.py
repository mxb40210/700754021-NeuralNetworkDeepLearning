"""
1. Implement Naïve Bayes method using scikit-learn library
   Use dataset available with name glass
   Use train_test_split to create training and testing part
   Evaluate the model on test part using score and classification_report(y_true, y_pred)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# Read glass csv
data_path = 'data/glass.csv'
data_df = pd.read_csv(data_path)

# Create dataframes for X (features), y (Target)
X = data_df.drop(columns=['Type'])
y = data_df['Type']  # Target

# Split the data into train and test sets using test_train_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Initialize the Naive Bayes classifier
naive_bayes_classifier = GaussianNB()

# Train
naive_bayes_classifier.fit(X_train, y_train)

# Predict
y_predictions = naive_bayes_classifier.predict(X_test)

# Evaluate
accuracy = round(naive_bayes_classifier.score(X_test, y_test) * 100, 2)
classification_report = classification_report(y_test, y_predictions)

print("Naive Bayes Classifier - Accuracy: {}" .format(accuracy))
print("Naive Bayes Classifier - Classification Report:\n{}" .format(classification_report))
