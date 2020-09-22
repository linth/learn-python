"""
Reference
    - https://ithelp.ithome.com.tw/articles/10187047
"""
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [10, 80], [8, 0], [8, 200], [5, 200], [7, 300], [8, 230], [7, 40], [9, 0], [6, 330], [9, 180]
])
y = np.array([469, 366, 371, 208, 246, 297, 363, 436, 198, 364])

lm = LinearRegression()
lm.fit(X, y)

# 新蛋糕店資料
to_be_predicted = np.array([
    [10, 110]
])
predicted_sales = lm.predict(to_be_predicted)

# 預測新蛋糕店的單月銷量
print(predicted_sales)


# 模型績效
# 複迴歸模型的績效（Performance）有
# 1) Mean squared error（MSE）
# 2) R-squared
# 3) Adjusted R-squared。
mse = np.mean((lm.predict(X) - y) ** 2)
r_squared = lm.score(X, y)
adj_r_squared = r_squared - (1 - r_squared) * (X.shape[1] / (X.shape[0] - X.shape[1] - 1))

# 印出模型績效
print(mse)
print(r_squared)
print(adj_r_squared)


from sklearn.feature_selection import f_regression
# 印出 p-value
# 複迴歸模型我們通常還會檢定變數的顯著性，以 P-value 是否小於 0.05（信心水準 95%）來判定。
print(f_regression(X, y)[1])

