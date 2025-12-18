import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("store_sales.csv")

pair_chart = sns.pairplot(data, hue="Category", palette='husl')

plt.show()
