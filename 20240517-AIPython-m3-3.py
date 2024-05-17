import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = sns.load_dataset("penguins")

sns.regplot(penguins_data, x='flipper_length_mm', y='body_mass_g')
plt.show()
