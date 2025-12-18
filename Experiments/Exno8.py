import seaborn as sns
import matplotlib.pyplot as plt

iris = sns. load_dataset('iris')

pair_chart = sns.pairplot(iris, hue="species", palette='husl')
pair_chart.savefig( 'irisPairChart.jpg', format="jpg", dpi=500)
plt.show()