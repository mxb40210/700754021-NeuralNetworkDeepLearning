"""
2. Implement linear SVM method using scikit library
   Use the same dataset above
   Use train_test_split to create training and testing part
   Evaluate the model on test part using score and classification_report(y_true, y_pred)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC, LinearSVC

# Read glass csv
data_path = 'data/glass.csv'
data_df = pd.read_csv(data_path)

# Create dataframes for X (features), y (Target)
X = data_df.drop(columns=['Type'])
y = data_df['Type']

# Split the data into train and test sets using test_train_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Initialize the Linear SVM
svm_classifier = LinearSVC()

# Train
svm_classifier.fit(X_train, y_train)

# Predict
y_predictions = svm_classifier.predict(X_test)

# Evaluate
accuracy = round(svm_classifier.score(X_test, y_test) * 100, 2)
classification_report = classification_report(y_test, y_predictions)

print("Linear SVM Classifier - Accuracy: {}" .format(accuracy))
print("Linear SVM Classifier - Classification Report:\n{}" .format(classification_report))

print('SVM has better accuracy than Naive Bayes due to non-linearity in the data')
