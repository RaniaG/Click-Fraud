'''
Created on Apr 20, 2018

@author: Rania
'''
import pandas as pd



df=pd.read_csv("./predictions/test_pred5.csv")
print("test pred ")
df2=pd.read_csv("./mergedfeatures/test2.csv")
print("test")
dfnew=pd.DataFrame(columns=["click_id","is_attributed"])
dfnew[['click_id']]=df2[['click_id']]
print("here")
dfnew[['is_attributed']]=df.iloc[:,1]
dfnew.sort_values("click_id", inplace=True)
dfnew.to_csv("./predictions/test_post4.csv",index=False)


