import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = sns.load_dataset("penguins")

sns.regplot(penguins_data, x='flipper_length_mm', y='body_mass_g')
plt.show()

numeric_penguins_data = penguins_data.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numeric_penguins_data.corr()

sns.heatmap(data=correlation_matrix, annot=True, fmt='.2f', cbar=False)
plt.show()