import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("HealthMetricsofPatients.csv")
data = pd.DataFrame(data)

pair_chart = sns.pairplot(data, hue="Risk_Level", palette='husl')

plt.show()