import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x = pd.read_csv("datasets/scaleddata.csv")
y = pd.read_csv("datasets/targetdata.csv")

if y.shape[1] >1:
    print("multi columns")
    y = y.iloc[:, 1]
    print("shape after: ",y.shape)
    print(y)

#print("df scaled: ", x)
print(x.shape)
print(y.shape)

y = y.values.ravel() # flatten the target array into 1D array

# Split dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

print(y_test.shape)
print(y_pred.shape)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")