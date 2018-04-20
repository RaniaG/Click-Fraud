import pandas as pd

import numpy as np
import gc
#11:29

t0=pd.read_csv("../test.csv")
t2=pd.read_csv("./predictions/test_count.csv")


print("t0")
print(t0.first)
print("t2")
print(t2.first)
t3=pd.merge(t0,t2,on="ip",sort=False)
print(t3.columns)  
print("merged")

print("t3")
t3=t3[['click_id','click_count','app_count','device_count','os_count','channel_count'\
       ,'app','device','os','channel']]
t3.to_csv("./mergedfeatures/test2.csv",index=False)


