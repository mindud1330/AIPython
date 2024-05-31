from sklearn import linear_model
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()

X = [[164], [179], [162], [170]]
y = [53, 63, 55, 59]

# linear model
regr.fit(X, y)

# draw scatter plot
plt.scatter(X, y)

# predict value
y_pred = regr.predict(X)
print(y_pred)

# draw plot
plt.plot(X, y_pred, color = 'blue', linewidth = 3)
plt.show()