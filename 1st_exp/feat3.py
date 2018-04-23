'''
Created on Apr 19, 2018

@author: Rania
'''
import pandas as pd

import numpy as np
import gc
from unittest.mock import inplace


df=pd.read_csv("./newfeatures/train_count8.csv")

newdf=pd.DataFrame(columns=['ip','click_count','device_click','app_click','os_click','channel_click'])

newdf[['ip','click_count']]=df[['ip','click_count']]
newdf['device_click']=df['device_count']/df['click_count']

newdf['os_click']=df['os_count']/df['click_count']
newdf['app_click']=df['app_count']/df['click_count']
newdf['channel_click']=df['channel_count']/df['click_count']


df=None
gc.collect()

df=pd.read_csv("../chunks/train-008.csv")
t3=pd.merge(df,newdf,on="ip",sort=False)
df=None
newdf=None
gc.collect()
print(t3.first)  
print("merged")

print("t3")
t3.drop(['device','click_time','attributed_time','ip'],axis=1,inplace=True)
t3.to_csv("./mergedfeatures/train8_count_r.csv",index=False)


