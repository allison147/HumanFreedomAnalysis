import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures

#IMPORT DATASET
df = pd.read_excel("C:/Users/Allison/Documents/Spring 2020/ENGI 305/HumanF reedom.xlsx", sheet_name="hfi_cc_2019", header=0)
pd.set_option('display.max_columns', None)
#DATA WRANGLING
df=df[["year","countries","hf_score","pf_score","ef_score","pf_rol","pf_ss","pf_movement","pf_religion","pf_association","pf_expression","pf_identity","ef_government","ef_legal","ef_money","ef_trade", "ef_regulation_credit_ownership"]]
df=df.replace('-',np.nan)
df=df.dropna(axis=0, how='any')
df[["hf_score"]].astype("float")
df=(df[df['year']==2017])


#MLR personal freedom
lm=LinearRegression()
Z=df[['pf_religion','pf_association','pf_expression']]
y=df[['pf_score']]
X_train, X_test, y_train, y_test=train_test_split(Z,y,test_size=0.2)
model=lm.fit(X_train,y_train)
predictions=lm.predict(X_test)
accuracy=metrics.r2_score(y,predictions)

plt.scatter(y, predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.show()
plt.scatter(y,predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.show()

print("intercept: ", lm.intercept_)
print("coefficient: ", lm.coef_)
print("Cross_predicted Accuracy: ", accuracy)
print("Score: ", model.score(X_test, y_test))
