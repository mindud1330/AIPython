import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = sns.load_dataset("penguins")

sns.barplot(x='species', y='body_mass_g', hue='sex', 
            data=penguins_data, errorbar='sd')
plt.show()

