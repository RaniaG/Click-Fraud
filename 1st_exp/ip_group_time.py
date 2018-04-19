'''
Created on Apr 14, 2018

@author: Rania
'''

import pandas as pd

import numpy as np

df=pd.read_csv("../modified/train0.csv")#11:30-11:35 done

print(df.columns)

#the required features
dfnew=pd.DataFrame(columns=["ip", "avg_click_pm","max_click_pm","var_click_pm","skew_click_pm",\
                             "avg_click_p5m","max_click_p5m","var_click_p5m","skew_click_p5m",\
                             "avg_click_p15m","max_click_p15m","var_click_p15m","skew_click_p15m",\
                             "avg_click_p1h","max_click_p1h","var_click_p1h","skew_click_p1h",\
                             "avg_click_p3h","max_click_p3h","var_click_p3h","skew_click_p3h",\
                             "avg_click_p6h","max_click_p6h","var_click_p6h","skew_click_p6h"\
                             ])


uniqueips=df['ip'].unique()
#dfnew['ip']=uniqueips

df1=df.copy()
print("starting to group by ip")

#------------------------------------------------------------------------------
#get number of clicks per minute:
print("number of clicks per minute")
dfn=df1.groupby(['ip','day','hour','minute']).size().reset_index(name='counts')



print(df1.columns)
print(df1.shape)
print(dfn.columns)
print(dfn.shape)
print(dfn.first)


#average
print("average")
dfnn=dfn.groupby(['ip']).mean().reset_index()

print(dfnn.first)

dfnew[['ip','avg_click_pm']]=dfnn[['ip','counts']]
#max
print("max")
dfnn=dfn.groupby(['ip']).max().reset_index()

print(dfnn.first)
dfnew['max_click_pm']=dfnn['counts']
print(dfnew.first)
#variance
print("variance")
dfnn=dfn.groupby(['ip']).var().reset_index()

print(dfnn.first)
dfnew['var_click_pm']=dfnn['counts']
print(dfnew.first)
#skewness
print("skewness")
dfnn=dfn.groupby(['ip']).skew().reset_index()
print(dfnn.first)
dfnew['skew_click_pm']=dfnn['counts']
print(dfnew.first)
#----------------------------------------------------------------------------------------
#get number of clicks per 5 min
print("number of clicks per 5 minutes")
df2=df.copy()

df2['minute'].loc[(df2['minute']>=0) & (df2['minute']<5)]=0
df2['minute'].loc[(df2['minute']>=5) & (df2['minute']<10)]=1
df2['minute'].loc[(df2['minute']>=10) & (df2['minute']<15)]=2
df2['minute'].loc[(df2['minute']>=15) & (df2['minute']<20)]=3
df2['minute'].loc[(df2['minute']>=20) & (df2['minute']<25)]=4
df2['minute'].loc[(df2['minute']>=25) & (df2['minute']<30)]=5
df2['minute'].loc[(df2['minute']>=30) & (df2['minute']<35)]=6
df2['minute'].loc[(df2['minute']>=35) & (df2['minute']<40)]=7
df2['minute'].loc[(df2['minute']>=40) & (df2['minute']<45)]=8
df2['minute'].loc[(df2['minute']>=45) & (df2['minute']<50)]=9
df2['minute'].loc[(df2['minute']>=50) & (df2['minute']<55)]=10
df2['minute'].loc[(df2['minute']>=55) & (df2['minute']<=60)]=11


print(df2.first)




dfn=df2.groupby(['ip','day','hour','minute']).size().reset_index(name='counts')



print(df2.columns)
print(df2.shape)
print(dfn.columns)
print(dfn.shape)
print(dfn.first)


#average
print("average")
dfnn=dfn.groupby(['ip']).mean().reset_index()

print(dfnn.first)

dfnew[['ip','avg_click_p5m']]=dfnn[['ip','counts']]
print(dfnew.first)
#max
print ("max")
dfnn=dfn.groupby(['ip']).max().reset_index()

print(dfnn.first)
dfnew['max_click_p5m']=dfnn['counts']
print(dfnew.first)
#variance
print("variance")
dfnn=dfn.groupby(['ip']).var().reset_index()

print(dfnn.first)
dfnew['var_click_p5m']=dfnn['counts']
print(dfnew.first)
#skewness
print("skewness")
dfnn=dfn.groupby(['ip']).skew().reset_index()

print(dfnn.first)
dfnew['skew_click_p5m']=dfnn['counts']
print(dfnew.first)


#--------------------------------------------------------------------------
#get number of clicks per 15 min
print("number of clicks per 15 minutes")
df3=df.copy()

df3['minute'].loc[(df3['minute']>=0) & (df3['minute']<15)]=0
df3['minute'].loc[(df3['minute']>=15) & (df3['minute']<30)]=1
df3['minute'].loc[(df3['minute']>=30) & (df3['minute']<45)]=2
df3['minute'].loc[(df3['minute']>=45) & (df3['minute']<=60)]=3



print(df3.first)




dfn=df3.groupby(['ip','day','hour','minute']).size().reset_index(name='counts')



print(df3.columns)
print(df3.shape)
print(dfn.columns)
print(dfn.shape)
print(dfn.first)


#average
print("average")
dfnn=dfn.groupby(['ip']).mean().reset_index()

print(dfnn.first)

dfnew[['ip','avg_click_p15m']]=dfnn[['ip','counts']]
print(dfnew.first)
#max
print("max")
dfnn=dfn.groupby(['ip']).max().reset_index()

print(dfnn.first)
dfnew['max_click_p15m']=dfnn['counts']
print(dfnew.first)
#variance
print("variance")
dfnn=dfn.groupby(['ip']).var().reset_index()

print(dfnn.first)
dfnew['var_click_p15m']=dfnn['counts']
print(dfnew.first)
#skewness
print ("skewness")
dfnn=dfn.groupby(['ip']).skew().reset_index()

print(dfnn.first)
dfnew['skew_click_p15m']=dfnn['counts']
print(dfnew.first)


#--------------------------------------------------------------------------------------
#get number of clicks per 1 hour
df4=df.copy()
print("number of clicks per hour")





print(df4.first)




dfn=df4.groupby(['ip','day','hour']).size().reset_index(name='counts')



print(df4.columns)
print(df4.shape)
print(dfn.columns)
print(dfn.shape)
print(dfn.first)


#average
print("average")
dfnn=dfn.groupby(['ip']).mean().reset_index()

print(dfnn.first)

dfnew[['ip','avg_click_p1h']]=dfnn[['ip','counts']]
print(dfnew.first)
#max
print("max")
dfnn=dfn.groupby(['ip']).max().reset_index()

print(dfnn.first)
dfnew['max_click_p1h']=dfnn['counts']
print(dfnew.first)
#variance
print("variance")
dfnn=dfn.groupby(['ip']).var().reset_index()

print(dfnn.first)
dfnew['var_click_p1h']=dfnn['counts']
print(dfnew.first)
#skewness
print("skewness")
dfnn=dfn.groupby(['ip']).skew().reset_index()

print(dfnn.first)
dfnew['skew_click_p1h']=dfnn['counts']
print(dfnew.first)

#------------------------------------------------------------------------------------
#clicks per 3 hours
print("number of clicks per 3 hours")

df5=df.copy()


df5['hour'].loc[(df5['hour']>=0) & (df5['hour']<3)]=0
df5['hour'].loc[(df5['hour']>=3) & (df5['hour']<6)]=1
df5['hour'].loc[(df5['hour']>=6) & (df5['hour']<9)]=2
df5['hour'].loc[(df5['hour']>=9) & (df5['hour']<12)]=3
df5['hour'].loc[(df5['hour']>=12) & (df5['hour']<15)]=4
df5['hour'].loc[(df5['hour']>=15) & (df5['hour']<18)]=5
df5['hour'].loc[(df5['hour']>=18) & (df5['hour']<21)]=6
df5['hour'].loc[(df5['hour']>=21) & (df5['hour']<=23)]=7

print(df5.first)




dfn=df5.groupby(['ip','day','hour']).size().reset_index(name='counts')



print(df5.columns)
print(df5.shape)
print(dfn.columns)
print(dfn.shape)
print(dfn.first)


#average
print ("average")
dfnn=dfn.groupby(['ip']).mean().reset_index()

print(dfnn.first)

dfnew[['ip','avg_click_p3h']]=dfnn[['ip','counts']]
print(dfnew.first)
#max
print("max")
dfnn=dfn.groupby(['ip']).max().reset_index()

print(dfnn.first)
dfnew['max_click_p3h']=dfnn['counts']
print(dfnew.first)
#variance
print("variance")
dfnn=dfn.groupby(['ip']).var().reset_index()

print(dfnn.first)
dfnew['var_click_p3h']=dfnn['counts']
print(dfnew.first)
#skewness
print("skewness")
dfnn=dfn.groupby(['ip']).skew().reset_index()

print(dfnn.first)
dfnew['skew_click_p3h']=dfnn['counts']
print(dfnew.first)

#------------------------------------------------------------------------------------
#clicks per 6 hours
print("number of clicks per 6 hours")

df6=df.copy()


df6['hour'].loc[(df6['hour']>=0) & (df6['hour']<3)]=0
df6['hour'].loc[(df6['hour']>=3) & (df6['hour']<6)]=1
df6['hour'].loc[(df6['hour']>=6) & (df6['hour']<9)]=2
df6['hour'].loc[(df6['hour']>=9) & (df6['hour']<12)]=3
df6['hour'].loc[(df6['hour']>=12) & (df6['hour']<15)]=4
df6['hour'].loc[(df6['hour']>=15) & (df6['hour']<18)]=5
df6['hour'].loc[(df6['hour']>=18) & (df6['hour']<21)]=6
df6['hour'].loc[(df6['hour']>=21) & (df6['hour']<=23)]=7

print(df6.first)




dfn=df6.groupby(['ip','day','hour']).size().reset_index(name='counts')



print(df6.columns)
print(df6.shape)
print(dfn.columns)
print(dfn.shape)
print(dfn.first)


#average
print("average")
dfnn=dfn.groupby(['ip']).mean().reset_index()

print(dfnn.first)

dfnew[['ip','avg_click_p6h']]=dfnn[['ip','counts']]
print(dfnew.first)
#max
print ("max")
dfnn=dfn.groupby(['ip']).max().reset_index()

print(dfnn.first)
dfnew['max_click_p6h']=dfnn['counts']
print(dfnew.first)
#variance
print("variance")
dfnn=dfn.groupby(['ip']).var().reset_index()

print(dfnn.first)
dfnew['var_click_p6h']=dfnn['counts']
print(dfnew.first)
#skewness
print("skewness")
dfnn=dfn.groupby(['ip']).skew().reset_index()

print(dfnn.first)
dfnew['skew_click_p6h']=dfnn['counts']
print(dfnew.first)

#------------------------------------------------------------------
print("saving to file")
dfnew.to_csv('train_time0.csv')
