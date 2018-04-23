import pandas as pd

import numpy as np
import gc
#11:29


t2=pd.read_csv("")

t0=pd.read_csv("")



print("t0")
print(t0.first)
print("t2")
print(t2.first)
t3=pd.merge(t0,t2,on="ip",sort=False)
print(t3.columns)  
print("merged")
t0=None
t2=None
gc.collect()
t3.to_csv("",index=False)


