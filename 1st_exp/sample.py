'''
Created on Apr 19, 2018

@author: Rania
'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import gc

def sample_split(df):

    print("sample start")
    #split dataset and random 
    train0, test0 = train_test_split(df.loc[df['is_attributed']==0], test_size=0.2)
    train1, test1 = train_test_split(df.loc[df['is_attributed']==1], test_size=0.2)
    print("split done")
    print(test0.shape)
    print(test1.shape)
    print(train0.shape)
    print(train1.shape)
    
    val=pd.concat([test0,test1])
    print(val.shape)
    test0=None
    test1=None
    gc.collect()
    train=pd.concat([train0,train1])
    train0=None
    train1=None
    gc.collect()
    print(train.shape)
    #shuffle 
    val = shuffle(val)
    train = shuffle(train)
    print(val.shape)
    print(train.shape)
    
    return val,train

def corr(df):
    
    corr = df.corr()
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)
    plt.show()