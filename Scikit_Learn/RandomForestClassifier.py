from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
X = [[1, 2, 3],
     [11,12,13]]
Y = [0,1]
print(clf.fit(X,Y))
