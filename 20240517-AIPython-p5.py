import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 15, 25, 30],
    'category': ['A', 'B', 'A', 'B', 'A']
})

sns.scatterplot(data = data, x = 'x', y = 'y', hue = 'category')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(title = 'Category')
plt.show()