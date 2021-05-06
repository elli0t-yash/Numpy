import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# clf = RandomForestClassifier(random_state=0)
# X = [[1, 2, 3],
#      [11,12,13]]
# Y = [0,1]
# print(clf.fit(X,Y))
# print(clf.predict(X))
# print(clf.predict([[4, 5, 6],[14, 15, 16]]))

# x = [[0, 15],
#      [1, -10]]
# print(StandardScaler().fit(x).transform(x))


# plotting graph
x = [i for i in range(10)]
y = [2*i for i in range(10)]
plt.plot(x, y)
plt.show()

plt.scatter(x,y)
plt.show()

# features are the independent variable or inputs 
# labels are the dependent variable or output
# no of features are called dimension
# no of labels are called instances
# features are represented by 'X' and labels are represented by 'y'

