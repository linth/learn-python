"""
References
- https://gist.github.com/yehjames/c9eed161c69b570730e37bce0c7faf4c#file-3-5-decision-tree-random-forest-ipynb
"""


from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


iris = datasets.load_iris()
# print('->', iris['data'])
# print('->', iris['target'])
# print('->', iris['target_names'])
# print('->', iris['DESCR'])


x = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print(x)
# print("target_names: " + str(iris['target_names']))

# y = pd.DataFrame(iris['target'], columns=['target'])
# iris_data = pd.concat([x, y], axis=1)
# iris_data = iris_data[['sepal length (cm)', 'petal length (cm)', 'target']]
# iris_data = iris_data[iris_data['target'].isin([0, 1])]
# iris_data.head(3)
#
# X_train, X_test, y_train, y_test = train_test_split(
#     iris_data[['sepal length (cm)',
#                'petal length (cm)']],
#     iris_data[['target']],
#     test_size=0.3,
#     random_state=0)
#
# tree = DecisionTreeClassifier(criterion='entropy', random_state=0)
# tree.fit(X_train, y_train)
# tree.predict(X_test)
# print(y_test['target'].values)
#
# error = 0
# for i, v in enumerate(tree.predict(X_test)):
#     if v != y_test['target'].values[i]:
#         print(i,v)
#         error += 1
# print(error)
#
# tree.score(X_test,y_test['target'])
#
# from matplotlib.colors import ListedColormap
#
# def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
#
#     # setup marker generator and color map
#     markers = ('s', 'x', 'o', '^', 'v')
#     colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
#     cmap = ListedColormap(colors[:len(np.unique(y))])
#
#     # plot the decision surface
#     x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
#     x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
#     xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
#                            np.arange(x2_min, x2_max, resolution))
#     Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
#     Z = Z.reshape(xx1.shape)
#     plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
#     plt.xlim(xx1.min(), xx1.max())
#     plt.ylim(xx2.min(), xx2.max())
#
#     for idx, cl in enumerate(np.unique(y)):
#         plt.scatter(x=X[y == cl, 0],
#                     y=X[y == cl, 1],
#                     alpha=0.6,
#                     c=cmap(idx),
#                     edgecolor='black',
#                     marker=markers[idx],
#                     label=cl)
#
#     # highlight test samples
#     if test_idx:
#         # plot all samples
#         if not versiontuple(np.__version__) >= versiontuple('1.9.0'):
#             X_test, y_test = X[list(test_idx), :], y[list(test_idx)]
#             warnings.warn('Please update to NumPy 1.9.0 or newer')
#         else:
#             X_test, y_test = X[test_idx, :], y[test_idx]
#
#         plt.scatter(X_test[:, 0],
#                     X_test[:, 1],
#                     c='',
#                     alpha=1.0,
#                     edgecolor='black',
#                     linewidths=1,
#                     marker='o',
#                     s=55, label='test set')
#
#
# plot_decision_regions(X_train.values, y_train['target'].values, classifier=tree)
# plt.xlabel('petal length [standardized]')
# plt.ylabel('petal width [standardized]')
# plt.legend(loc='upper left')
# plt.tight_layout()
# plt.show()
