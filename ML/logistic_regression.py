"""
Reference
    - https://ithelp.ithome.com.tw/articles/10187047
"""
# Logistic 迴歸雖然冠有迴歸的名稱，但實際上是一個二元分類（Binary classification）演算法嗎？
# Logistc 迴歸是我們建立的第一個分類器（Classifier）。
# 分類（Classification）與迴歸（Regression）都屬於監督式學習（Supervised learning），
# 一個預測類別目標變數，一個預測連續型目標變數。
import pandas as pd
import numpy as np
from sklearn import preprocessing, linear_model

path = 'data\\train.csv'
titanic_train = pd.read_csv(path)
print(titanic_train)


# 將 Age 遺漏值以 median 填補
age_median = np.nanmedian(titanic_train["Age"])
new_Age = np.where(titanic_train["Age"].isnull(), age_median, titanic_train["Age"])
titanic_train["Age"] = new_Age
# print(titanic_train)


# 創造 dummy variables
label_encoder = preprocessing.LabelEncoder()
encoded_Sex = label_encoder.fit_transform(titanic_train["Sex"])


# 建立 train_X
train_X = pd.DataFrame(
                        # [titanic_train["Pclass"],
                        [
                            # titanic_train["Pclass"],
                            # encoded_Sex,
                            titanic_train["Parch"]
                        ]
).T


# 建立模型
logistic_regr = linear_model.LogisticRegression()
logistic_regr.fit(train_X, titanic_train["Survived"])

# 印出係數
print('印出係數', logistic_regr.coef_)

# 印出截距
print('印出截距', logistic_regr.intercept_)


# 印出 p-value
from sklearn.feature_selection import f_regression
print('p-value', f_regression(train_X, titanic_train["Survived"])[1])


# 計算準確率
survived_predictions = logistic_regr.predict(train_X)
accuracy = logistic_regr.score(train_X, titanic_train["Survived"])
print('計算準確率', accuracy)
