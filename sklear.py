from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris  = load_iris()
# print(iris.data)
# print(iris.target)
# print(iris.target_names)
# print(iris.feature_names)
# print(iris.data.shape)

X = iris.data
t= iris.feature_names
y = iris.target
z = iris.target_names

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)
x_test = [[5.1,3.5,1.4,0.5]]



def check(x):
    result = (knn.predict(x))
    for i in range(3):
        if i == int(result):
            print(z[i])


check(x_test)


