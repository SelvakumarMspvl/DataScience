import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


iris = sns.load_dataset('iris')

x = iris.drop('species', axis=1)

k_mean = KMeans(n_clusters = 3,random_state = 42)
iris['cluster'] = k_mean.fit_predict(x)

print('Cluster Center:\n', k_mean.cluster_centers_)
plt.figure(figsize=(12,8))
plt.scatter(
    x.iloc[:,0],
    x.iloc[:,1],
    c = iris['cluster'],
    cmap = 'viridis',
    s = 50
)
plt.title('K-Mean Clustering on iris dataset')
plt.xlabel('sepal length(cm)')
plt.ylabel('sepal width(cm)')

print(iris.groupby(['cluster', 'species']).size())

plt.show()