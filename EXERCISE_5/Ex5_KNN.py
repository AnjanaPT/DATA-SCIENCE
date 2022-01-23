'''To Implement KNN Algorithm'''
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
print("-------------------------------------------------------------------")
print("Extracting Features\n")
f_name=iris.feature_names
print(f_name)
print("-------------------------------------------------------------------")
print("Extracting Targets\n")
t_name=iris.target_names
print(t_name)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
print("-------------------------------------------------------------------")
print("Number of rows of columns in test data\n")
print(x_test.shape)
print("-------------------------------------------------------------------")
print("Number of rows of columns in train data\n")
print(x_train.shape)
from sklearn.neighbors import KNeighborsClassifier
c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train,y_train)
y_pred=c_knn.predict(x_test)
from sklearn import metrics
print("-------------------------------------------------------------------")
print("Accuracy\n")
print(metrics.accuracy_score(y_test,y_pred))
sample=[[10,10,5,2]]
pred=c_knn.predict(sample)
pred_val=[iris.target_names[p] for p in pred]
print("-------------------------------------------------------------------")
print("Predicted Values\n")
print(pred_val)
print("-------------------------------------------------------------------")
