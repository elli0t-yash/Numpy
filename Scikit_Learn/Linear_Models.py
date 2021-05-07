from sklearn import linear_model
import numpy as np

reg = linear_model.LinearRegression()
print(reg.fit([[0,0], [1,1], [2,2]], [0, 1, 2]))

print(reg.coef_)

reg0 = linear_model.Ridge(alpha=.5)
print(reg0.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1]))
print(reg0.coef_)
print(reg0.intercept_)

reg1 = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
print(reg1.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1]))
print(reg1.alpha_)

reg2 = linear_model.Lasso(alpha=0.1)
print(reg2.fit([[0, 0], [1,1]], [0, 1]))
print(reg2.predict([[1, 1]]))