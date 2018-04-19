import pandas as pd

import numpy as np
import gc
#11:29

t0=pd.read_csv("../chunks/train-000.csv")
colnames = ['ip','avg_click_p3h','max_click_p3h', 'var_click_p3h', 'skew_click_p3h']
t2=pd.read_csv("./newfeatures/train_time0.csv")
#t2=pd.read_csv("./newfeatures/train_count0.csv")
t2=t2[colnames]

print("t0")
print(t0.first)
print("t2")
print(t2.first)
t3=pd.merge(t0,t2,on="ip",sort=False)
print(t3.first)  
print("merged")

print("t3")
t3.to_csv("./mergedfeatures/train0_time5.csv")


