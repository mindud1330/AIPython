import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'B', 'B'],
    'value': [10, 20, 15, 25, 30, 12, 18, 22, 28, 35]
})

sns.countplot(data=data, x='category', hue='category')
plt.show()