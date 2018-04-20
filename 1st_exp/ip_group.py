'''
Created on Apr 13, 2018

@author: Rania
'''
import pandas as pd

import numpy as np

df=pd.read_csv("../test.csv")#8
print("file loaded")

print(df.columns)
uniqueips=df['ip'].unique()
print(len(uniqueips))
dfnew=pd.DataFrame(columns=["ip", "click_count","app_count", "device_count","os_count","channel_count"])


#click count
print("click count")
df1=df.copy()
dfn=df1.groupby(['ip']).size().reset_index(name='counts')
print(dfn.first)
dfnew[['ip','click_count']]=dfn[['ip','counts']]
print(dfnew.first)

#------------------------------------------------------------
#apps count
print("app count")
df2=df.copy()
dfn=df2.groupby(['ip','app']).size().reset_index(name='counts')
print(dfn.first)
dfnn=dfn.groupby(['ip']).agg(['count']).reset_index()
print(dfnn.first)
dfnew[['app_count']]=dfn[['counts']]
print(dfnew.first)
#------------------------------------------------------------

#device count
print("device count")
df3=df.copy()
dfn=df3.groupby(['ip','device']).size().reset_index(name='counts')
print(dfn.first)
dfnn=dfn.groupby(['ip']).agg(['count']).reset_index()
print(dfnn.first)
dfnew[['device_count']]=dfn[['counts']]
print(dfnew.first)
#------------------------------------------------------------
#channel count
print("channel count")
df4=df.copy()
dfn=df4.groupby(['ip','channel']).size().reset_index(name='counts')
print(dfn.first)
dfnn=dfn.groupby(['ip']).agg(['count']).reset_index()
print(dfnn.first)
dfnew[['channel_count']]=dfn[['counts']]
print(dfnew.first)

#------------------------------------------------------------
#os count
print("os count")
df5=df.copy()
dfn=df5.groupby(['ip','channel']).size().reset_index(name='counts')
print(dfn.first)
dfnn=dfn.groupby(['ip']).agg(['count']).reset_index()
print(dfnn.first)
dfnew[['os_count']]=dfn[['counts']]
print(dfnew.first)






print("saving to file")
dfnew.to_csv('test_count.csv',index=False)

