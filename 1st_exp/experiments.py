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

from sklearn.externals import joblib
import gc
from sample import sample_split,corr

def train(filename,modelname,t):
        
    df=pd.read_csv(filename)
    print(df.columns)
    print(df.dtypes)
    print(df.first)
    if(t):
        df=df.drop(['ip','click_time','attributed_time'],axis=1)
    #corr(df)
    
    
    val,train=sample_split(df)
    df= None 
    gc.collect()
    print("sampling done")
    y_train=train[['is_attributed']]
    x_train=train.drop(['is_attributed'],axis=1)
    
    y_val=val[['is_attributed']]
    x_val=val.drop(['is_attributed'],axis=1)
    
    print(x_train.shape)
    print(y_train.shape)
    print(x_val.shape)
    print(y_val.shape)
    
    estimator =xgb.XGBClassifier(max_depth=3, learning_rate=1,
                               n_estimators=1000, objective='binary:logistic',
                                booster='gbtree', gamma=1,
                                 min_child_weight=15, subsample=1,
                                  colsample_bytree=1,
                               reg_lambda=10)
    
    estimator.fit(x_train, y_train, eval_set=[(x_train, y_train), (x_val, y_val)], eval_metric='auc',verbose=True,early_stopping_rounds= 50)
    print(estimator)
    joblib.dump(estimator, modelname)
    print(y_train.shape)
    xgb.plot_importance(estimator)
    plt.show()
    
    y_pred=estimator.predict(x_train)
    
    
    
    fpr, tpr, _ = roc_curve(y_train, y_pred)
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
    
#train("train-000.csv","originalFeatures_18mil",False)
#train("./mergedfeatures/train0_count.csv","countFeatures_18mil",False)
#train("./mergedfeatures/train0_time5.csv","timeFeatures5_18mil",True)
#train("./mergedfeatures/train0_count_r.csv",True)

train("./mergedfeatures/train_ip_feat0.csv","ip_Features_18mil",False)
