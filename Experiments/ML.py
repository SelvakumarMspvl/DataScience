import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn. tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

iris = sns. load_dataset("iris")
x = iris.drop( 'species', axis=1)
y = iris['species' ]

x_train, x_test, y_train, y_test = train_test_split(  x, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model. fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy: ", accuracy_score(y_test, y_pred))

plt.figure(figsize=(12,8))
plot_tree(model,filled = True, feature_names= x.columns, class_names=model.classes_)
plt.title("Decision Tree -Iris Dataset")
plt.show()