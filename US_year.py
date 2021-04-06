import pandas as pd
import numpy as np

#IMPORT DATASET
df = pd.read_excel("C:/Users/Allison/Documents/Spring 2020/ENGI 305/humanfreedom.xlsx", sheet_name="hfi_topQuartile", header=0)
pd.set_option('display.max_columns', None)

#DATA WRANGLING
df=df[["year","countries","hf_score","pf_score","ef_score","pf_rol","pf_ss","pf_movement","pf_religion","pf_association","pf_expression","pf_identity","ef_government","ef_legal","ef_money","ef_trade", "ef_regulation_credit_ownership"]]
df=df.replace('-',np.nan)
df=df.dropna(axis=0, how='any')
df[["hf_score"]].astype("float")
df=(df[df['year']==2017])

#COMPARING US INDICES WITH OTHER COUNTRIES
# bin all scores
bins=np.linspace(min(df['ef_regulation_credit_ownership']),max(df['ef_regulation_credit_ownership']),4)
group_names=["low","med",'high']
df["credit"]=pd.cut(df["ef_regulation_credit_ownership"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['ef_trade']),max(df['ef_trade']),4)
group_names=["low","med",'high']
df["trade"]=pd.cut(df["ef_trade"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['ef_money']),max(df['ef_money']),4)
group_names=["low","med",'high']
df["money"]=pd.cut(df["ef_money"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['ef_legal']),max(df['ef_legal']),4)
group_names=["low","med",'high']
df["legal"]=pd.cut(df["ef_legal"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['ef_government']),max(df['ef_government']),4)
group_names=["low","med",'high']
df["government"]=pd.cut(df["ef_government"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['pf_identity']),max(df['pf_identity']),4)
group_names=["low","med",'high']
df["identity"]=pd.cut(df["pf_identity"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['pf_expression']),max(df['pf_expression']),4)
group_names=["low","med",'high']
df["expression"]=pd.cut(df["pf_expression"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['pf_association']),max(df['pf_association']),4)
group_names=["low","med",'high']
df["association"]=pd.cut(df["pf_association"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['pf_religion']),max(df['pf_religion']),4)
group_names=["low","med",'high']
df["Religion"]=pd.cut(df["pf_religion"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['pf_movement']),max(df['pf_movement']),4)
group_names=["low","med",'high']
df["Movement"]=pd.cut(df["pf_movement"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['pf_ss']),max(df['pf_ss']),4)
group_names=["low","med",'high']
df["Safety and Security"]=pd.cut(df["pf_ss"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['pf_rol']),max(df['pf_rol']),4)
group_names=["low","med",'high']
df["ROL"]=pd.cut(df["pf_rol"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['hf_score']),max(df['hf_score']),4)
group_names=["low","med",'high']
df["human_freedom"]=pd.cut(df["hf_score"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['ef_score']),max(df['ef_score']),4)
group_names=["low","med",'high']
df["economic_freedom"]=pd.cut(df["ef_score"], bins, labels=group_names, include_lowest=True)

bins=np.linspace(min(df['pf_score']),max(df['pf_score']),4)
group_names=["low","med",'high']
df["personal_freedom"]=pd.cut(df["pf_score"], bins, labels=group_names, include_lowest=True)

#display all bin scores
dc=df[["countries","human_freedom","economic_freedom","personal_freedom","ROL","Safety and Security","Movement","Religion","association","expression","identity","government","legal","money","trade", "credit"]]
dc=(dc[dc['countries']=="United States"])
print(dc)
