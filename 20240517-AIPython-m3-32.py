import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = sns.load_dataset("penguins")
numeric_penguins_data = penguins_data.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numeric_penguins_data.corr()

sns.heatmap(data=correlation_matrix, annot=True, fmt='.2f', cbar=False)
plt.show()