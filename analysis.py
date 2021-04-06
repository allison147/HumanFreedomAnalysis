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
df = pd.read_excel("C:/Users/Allison/Documents/Spring 2020/ENGI 305/humanfreedom.xlsx", sheet_name="hfi_cc_2019", header=0)
pd.set_option('display.max_columns', None)
#DATA WRANGLING
df=df[["year","countries","hf_score","pf_score","ef_score","pf_rol","pf_ss","pf_movement","pf_religion","pf_association","pf_expression","pf_identity","ef_government","ef_legal","ef_money","ef_trade", "ef_regulation_credit_ownership"]]
df=df.replace('-',np.nan)
df=df.dropna(axis=0, how='any')
df[["hf_score"]].astype("float")

(df.describe())
df=(df[df["year"] == 2017])


# ANALYSIS

#Safety and Security Model
y=df["pf_ss"]
x=df["ef_legal"]
X_train, X_test, y_train,y_test = train_test_split(x,y,test_size=0.4)
f=np.polyfit(X_train,y_train,2)
p=np.poly1d(f)
R2=metrics.r2_score(y_test,p(X_test))
mse=mean_squared_error(y_test,p(X_test))
pcoeff0=stats.pearsonr(df["pf_ss"], df["ef_legal"])
print("R2: ",R2)
print("MSE: ", mse)
print("Safety/Security and Legal Corr.: ", pcoeff0)

plt.scatter(x,y)
plt.title("The effect of the Legal System on Safety and Security")
plt.ylabel("Safety and Security")
plt.xlabel("Strength of the Legal System")
plt.plot(x,p(x))
plt.show()


#comparing  religion and expression
y=df[["pf_religion"]]
x=df[["pf_expression"]]
plt.scatter(x,y)
plt.title("The Effect of Freedom of Expression on Freedom of Religion")
plt.ylabel("Freedom of Expression")
plt.xlabel("Freedom of Religion")
plt.show()
pcoeff1=stats.pearsonr(df["pf_religion"], df["pf_expression"])
print("Religion and Expression Corr.: ",pcoeff1)

#comparing personal and economic freedom
y=df[["pf_score"]]
x=df[["ef_score"]]
plt.scatter(x,y)
plt.title("Economic vs. Personal Freedom")
plt.ylabel("Personal Freedom")
plt.xlabel("Economic Freedom")
plt.show()
pcoeff2=stats.pearsonr(df["pf_score"], df["ef_score"])
print("Economic and Personal Corr.: ", pcoeff2)

# comparing expression and association
y=df[["pf_association"]]
x=df[["pf_expression"]]
plt.scatter(x,y)
plt.title("Freedom of Expression vs. Association")
plt.ylabel("Freedom of Expression")
plt.xlabel("Freedom of Association")
plt.show()
pcoeff3=stats.pearsonr(df["pf_association"], df["pf_expression"])
print("Association and Expression Corr.: ", pcoeff3)


