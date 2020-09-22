"""
Reference:
    - https://ithelp.ithome.com.tw/articles/10186905
"""
from sklearn import datasets
import pandas as pd


iris = datasets.load_iris()
house = datasets.load_boston()
patient = datasets.load_diabetes()

# print(type(iris.data))
# print(iris.feature_names)
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
# iris_df.ix[:, "species"] = iris.target
# print(iris_df, iris)

# data
import numpy as np
from sklearn.linear_model import LinearRegression

# 轉換維度
temperatures = np.array([29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])
iced_tea_sales = np.array([77, 62, 93, 84, 59, 64, 80, 75, 58, 91, 51, 73, 65, 84])

lm = LinearRegression()
lm.fit(np.reshape(temperatures, (len(temperatures), 1)),
       np.reshape(iced_tea_sales, len(iced_tea_sales), 1))
# print('印出係數 coef_: ', lm.coef_)
# print('印出截距 intercept_: ', lm.intercept_)


# 利用線性迴歸分析模型預測 - 預測的冰紅茶銷量
to_be_predicted = np.array([25, 28, 30, 33, 35])
print('to_be_predicted', to_be_predicted)
predicted_sales = lm.predict(
    np.reshape(to_be_predicted, (len(to_be_predicted), 1))
)

print(predicted_sales)


# 線性迴歸視覺化
import matplotlib.pyplot as plt
plt.scatter(temperatures, iced_tea_sales, color='black')
plt.plot(temperatures,
         lm.predict(
             np.reshape(temperatures, (len(temperatures), 1))),
         color='blue',
         linewidth=3)
plt.plot(to_be_predicted,
         predicted_sales,
         color='red',
         marker='^',
         markersize=10)
plt.xticks(())
plt.yticks(())
plt.show()


# 模型績效
mse = np.mean((lm.predict(temperatures) - iced_tea_sales) ** 2)
r_squared = lm.score(temperatures, iced_tea_sales)

# 印出模型績效
print(mse)
print(r_squared)
