'''
Created on Apr 19, 2018

@author: Rania
'''
import pandas as pd

import numpy as np
import gc

df=pd.read_csv("./mergedfeatures/train0_count.csv")
print(df.columns)

df=df.drop(['attributed_time','click_time'],axis=1)
df2=df.copy()

df3=df2.groupby(['ip','app']).size().reset_index(name='counts')
print(df3.columns)
df3.rename( columns={"counts": "ip_app_count"},inplace=True)
print(df3.columns)
df4=df2.groupby(['ip','os']).size().reset_index(name='counts')
print(df4.columns)
df4.rename( columns={"counts": "ip_os_count"},inplace=True)
print(df4.columns)
df5=df2.groupby(['ip','channel']).size().reset_index(name='counts')
print(df5.columns)
df5.rename( columns={"counts": "ip_channel_count"},inplace=True)
print(df5.columns)
df6=df2.groupby(['ip','device']).size().reset_index(name='counts')
print(df6.columns)
df6.rename( columns={"counts": "ip_device_count"},inplace=True)
print(df6.columns)

dfnew=pd.merge(df,df3,on=['ip','app'],sort=False)
df=None
df2=None
df3=None
gc.collect()
print("dfone 1")
dfnew1=pd.merge(dfnew,df4,on=['ip','os'],sort=False)
dfnew=None
df4=None
gc.collect()
print("dfone 2")
dfnew2=pd.merge(dfnew1,df5,on=['ip','channel'],sort=False)
df5=None
dfnew1=None
gc.collect()
print("dfone 3")
dfnew3=pd.merge(dfnew2,df6,on=['ip','device'],sort=False)
df6=None
dfnew2=None
gc.collect()
print("dfone 4")
dfnew3=dfnew3[['app','channel','os','device','is_attributed','click_count','ip_app_count'\
               ,'ip_os_count','ip_channel_count']]
dfnew3.to_csv("./mergedfeatures/train_ip_feat0.csv")



