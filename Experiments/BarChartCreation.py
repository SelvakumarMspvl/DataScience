import seaborn as sns
import matplotlib.pyplot as plt

dataSet = sns.load_dataset('iris')

setosa = dataSet[dataSet['species'] == 'setosa']

AverageValue = setosa.mean(numeric_only=True)
AverageValue.plot(kind = 'bar',color = 'lightblue',edgecolor= 'black',linewidth = 2)
plt.title("Average Feature Values")
plt.xlabel("Feature Values")
plt.ylabel("Average Values")
plt.show()