"""PCA tutorial from
https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60"""

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, names=['sepal length', 'sepal width', 'petal length',
                             'petal width', 'target'])
# print(df)

"""
Standardize the Data

PCA is effected by scale so you need to scale the features in your data before applying PCA. 
"""
from sklearn.preprocessing import StandardScaler

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values
y = df.loc[:, ['target']].values

x = StandardScaler().fit_transform(x)

"""
PCA Projection to 2D

The original data has 4 columns (sepal length, sepal width, petal length, 
and petal width). In this section, the code projects the original data which is 
4 dimensional into 2 dimensions.
"""
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents,
                           columns=['principal component 1',
                                    'principal component 2'])
# print(principalDf.shape[0])
# print(df.shape[0])

finalDf = pd.concat([principalDf, df[['target']]], axis=1)

"""Visualize 2D Projection"""
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']

for target, color in zip(targets, colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c=color
               , s=50)
ax.legend(targets)
ax.grid()
# plt.show()

print(pca.explained_variance_ratio_)
