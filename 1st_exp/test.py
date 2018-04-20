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



df=pd.read_csv("./mergedfeatures/test2.csv")

print(df.columns)

df.drop(['click_id'],axis=1,inplace=True)
print(df.columns)
model = joblib.load("./models/countFeatures_18mil")
print("model loaded")

y_pred=model.predict_proba(df)
print("prediction done")
df2=pd.DataFrame(y_pred)

print(df2.first)
print(df2.columns)
df2.to_csv("./predictions/test_pred4.csv",index=False)
'''
df=pd.read_csv("./mergedfeatures/train8_count.csv")

print(df.columns)

y_test=df[['is_attributed']]
x_test=df.drop(['is_attributed'],axis=1)

model = joblib.load("countFeatures_18mil")
print("model loaded")

y_pred=model.predict_proba(x_test)
print("prediction done")


fpr, tpr, _ = roc_curve(y_test, y_pred[:,1])
roc_auc = auc(fpr, tpr)
print(roc_auc)

plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([-0.02, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.legend(loc="lower right")
plt.show()
'''
