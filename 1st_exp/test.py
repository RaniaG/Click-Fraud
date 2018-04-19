'''
Created on Apr 19, 2018

@author: Rania
'''

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score , roc_auc_score ,roc_curve, auc
import xgboost as xgb
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.externals import joblib
import gc



df1=pd.read_csv("../test.csv")

print(df1.columns)

df2=pd.read_csv("../t1.csv")

print(df2.columns)
'''
model = joblib.load("../countFeatures_18mil")

df1.drop(['click_id'])
y_pred=model.predict(df1)

fpr, tpr, _ = roc_curve(df2, y_pred)
roc_auc = auc(fpr, tpr)
print(roc_auc)
'''