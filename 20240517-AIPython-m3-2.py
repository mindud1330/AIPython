import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = sns.load_dataset("penguins")

sns.pairplot(penguins_data, hue='species')
plt.show()

