from sklearn import linear_model
import matplotlib.pyplot as plt

prod_area = [[2.1], [10], [3], [1], [3.5], [5], [8]]
production = [64.9, 292.6, 85.9, 30.92, 110.5, 163.4, 163.4]

# draw scatter plot
plt.scatter(prod_area, production)

# linear model
regr = linear_model.LinearRegression()
regr.fit(prod_area, production)
production_pred = regr.predict(prod_area)

# draw linear plot 
plt.plot(prod_area, production_pred, color = 'blue', linewidth = 3)

# predict value
input_data = [[7], [12]]
result = regr.predict(input_data)
print(result)

# show plot
plt.show()
