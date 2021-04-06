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
df=(df[df['year']==2017])
da=df[["hf_score","pf_score","ef_score","pf_rol","pf_ss","pf_movement","pf_religion","pf_association","pf_expression","pf_identity","ef_government","ef_legal","ef_money","ef_trade", "ef_regulation_credit_ownership"]]
# bin all scores
bins=np.linspace(min(df['hf_score']),max(df['hf_score']),4)
group_names=["low","med",'high']
df["hf_binned"]=pd.cut(df["hf_score"], bins, labels=group_names, include_lowest=True)


#display all bin scores
dc=df[["countries","hf_binned","ef_binned","pf_binned"]]
dc=(dc[dc['countries']=="United States"])
print(dc)