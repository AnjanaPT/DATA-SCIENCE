from sklearn.datasets import load_iris
data=load_iris()
x=data.data
y=data.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
from sklearn.metrics import accuracy_score
print("Accuracy on Train Using GINI : ",accuracy_score(y_true=y_train,y_pred=classifier.predict(x_train)))
print("Accuracy on Test Using GINI  : ",accuracy_score(y_true=y_test,y_pred=y_pred))

import matplotlib.pyplot as plt
from sklearn import tree
plt.figure(figsize=(15,15))
tree.plot_tree(classifier,fontsize=10,filled=True,rounded=True,feature_names = data.feature_names, class_names = data.target_names)
plt.show()