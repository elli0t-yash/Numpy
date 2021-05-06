import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris, make_regression, fetch_california_housing
from sklearn.model_selection import train_test_split, cross_validate, RandomizedSearchCV
from sklearn.metrics import accuracy_score
from scipy.stats import randint

#? clf = RandomForestClassifier(random_state=0)
#? X = [[1, 2, 3],
#?      [11,12,13]]
#? Y = [0,1]
#? print(clf.fit(X,Y))
#? print(clf.predict(X))
#? print(clf.predict([[4, 5, 6],[14, 15, 16]]))

#? x = [[0, 15],
#?      [1, -10]]
#? print(StandardScaler().fit(x).transform(x))


#! plotting graph
#? x = [i for i in range(10)]
#? y = [2*i for i in range(10)]
#? plt.plot(x, y)
#? plt.show()

#? plt.scatter(x,y)
#? plt.show()

#! features are the independent variable or inputs 
#! labels are the dependent variable or output
#! no of features are called dimension
#! no of labels are called instances
#! features are represented by 'X' and labels are represented by 'y'

#! preprocessing and estimators

#! creating a pipeline
#? pipe = make_pipeline(
#?     StandardScaler(),
#?     LogisticRegression()
#? )

#! load the iris dataset and split it into train test sets
#? X, y = load_iris(return_X_y=True)
#? X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#! fit the whole pipeline 
#? print(pipe.fit(X_train, y_train))

#? print("accuracy: ",accuracy_score(pipe.predict(X_test), y_test))

#! Model evalution
#? X, y = make_regression(n_samples=1000, random_state=0)
#? lr = LinearRegression()
#? result = cross_validate(lr, X, y)
#? print(result['test_score'])

#! Automatic parameter searches
X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#! define the parameter space that will be searched over 
param_distributions = {
    'n_estimators': randint(1, 5),
    'max_depth': randint(5, 10)
} 

#! now create a searchCV object and fit it to the data
search = RandomizedSearchCV(
    estimator=RandomForestRegressor(random_state=0),
    n_iter=5,
    param_distributions=param_distributions,
    random_state=0
)

print(search.fit(X_train, y_train))

print(search.best_params_)

#! the search object now acts like a normal random forest estimator with max_depth = 9 and n_estimators
print(search.score(X_test, y_test))