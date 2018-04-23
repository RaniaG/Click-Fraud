import pandas as pd
from boosting import boosting
import pickle

train = pd.read_csv('../Data/train.csv', nrows=18000000)

train.columns = ['ip', 'app', 'device', 'os', 'channel', 'click_time', 'attributed_time', 'is_attributed']
y_train=train['is_attributed']
x_train=train.drop(['is_attributed','attributed_time'],axis=1)

# handel time
x_train['click_time'] = pd.to_datetime(x_train['click_time'])
x_train['month']= x_train['click_time'].dt.month.astype('uint8')
x_train['day']= x_train['click_time'].dt.day.astype('uint8')
x_train['hour']= x_train['click_time'].dt.hour.astype('uint8')
x_train['minute']= x_train['click_time'].dt.minute.astype('uint8')
x_train['second']= x_train['click_time'].dt.second.astype('uint8')
x_train.drop(['click_time'],axis=1,inplace=True)

# number of clicks for each channel
ch_count=x_train.groupby(['channel'])['ip'].count().reset_index()
ch_count.columns = ['channel', 'click_channel']
x_train = pd.merge(x_train, ch_count, on=['channel'], how='left', sort=False)



#how many ips with this channel
ip_per_ch=x_train.groupby(['ip','channel']).size().reset_index()
ip_per_ch.columns = ['ip','channel', 'channel_ip']
ip_per_ch=ip_per_ch.groupby(['channel']).agg(['count']).reset_index() #.size() or .count
ip_per_ch=ip_per_ch.drop(['ip'],axis=1)
ip_per_ch.columns = ['channel', 'channel_#ip']
x_train = pd.merge(x_train, ip_per_ch, on=['channel'], how='left', sort=False)
#how many apps with this channel
app_per_ch=x_train.groupby(['app','channel']).size().reset_index()
app_per_ch.columns = ['app','channel', 'channel_app']
app_per_ch=app_per_ch.groupby(['channel']).agg(['count']).reset_index()
app_per_ch=app_per_ch.drop(['app'],axis=1)
app_per_ch.columns = ['channel', 'channel_#app']
x_train = pd.merge(x_train, app_per_ch, on=['channel'], how='left', sort=False)
#how many oss with this channel
os_per_ch=x_train.groupby(['os','channel']).size().reset_index()
os_per_ch.columns = ['os','channel', 'channel_os']
os_per_ch=os_per_ch.groupby(['channel']).agg(['count']).reset_index()
os_per_ch=os_per_ch.drop(['os'],axis=1)
os_per_ch.columns = ['channel', 'channel_#os']
x_train = pd.merge(x_train, os_per_ch, on=['channel'], how='left', sort=False)
#how many devices with this channel
d_per_ch=x_train.groupby(['device','channel']).size().reset_index()
d_per_ch.columns = ['device','channel', 'channel_device']
d_per_ch=d_per_ch.groupby(['channel']).agg(['count']).reset_index()
d_per_ch=d_per_ch.drop(['device'],axis=1)
d_per_ch.columns = ['channel', 'channel_#device']
x_train = pd.merge(x_train, d_per_ch, on=['channel'], how='left', sort=False)
#
# number of clicks per hour for each channel
ch_hour=x_train.groupby(['channel','day','hour']).size().reset_index()
ch_hour.columns = ['channel','day','hour', 'channels_per_hour']
ch_hour=ch_hour.groupby(['channel']).max().reset_index()
ch_hour=ch_hour.drop(['day','hour'],axis=1)
x_train = pd.merge(x_train, ch_hour, on=['channel'], how='left', sort=False)
# #################################################################
x_train['3hour']=pd.DataFrame(columns=["3hours"])

x_train['3hour'].loc[(x_train['hour']>=0) & (x_train['hour']<3)]=0
x_train['3hour'].loc[(x_train['hour']>=3) & (x_train['hour']<6)]=1
x_train['3hour'].loc[(x_train['hour']>=6) & (x_train['hour']<9)]=2
x_train['3hour'].loc[(x_train['hour']>=9) & (x_train['hour']<12)]=3
x_train['3hour'].loc[(x_train['hour']>=12) & (x_train['hour']<15)]=4
x_train['3hour'].loc[(x_train['hour']>=15) & (x_train['hour']<18)]=5
x_train['3hour'].loc[(x_train['hour']>=18) & (x_train['hour']<21)]=6
x_train['3hour'].loc[(x_train['hour']>=21) & (x_train['hour']<=23)]=7
# number of clicks per 3hours for each channel
ch_3h=x_train.groupby(['channel','day','3hour']).size().reset_index()
ch_3h.columns = ['channel','day','3hour', 'channels_per_3h']
ch_3h=ch_3h.groupby(['channel']).max().reset_index()
ch_3h=ch_3h.drop(['day','3hour'],axis=1)
x_train = pd.merge(x_train, ch_3h, on=['channel'], how='left', sort=False)
x_train=x_train.drop(['3hour'],axis=1)

#################################################################
# number of clicks per minute for each channel
ch_min=x_train.groupby(['channel','day','hour','minute']).size().reset_index()
ch_min.columns = ['channel','day','hour','minute', 'channels_per_min']
ch_min=ch_min.groupby(['channel']).max().reset_index()
ch_min=ch_min.drop(['day','hour','minute'],axis=1)
x_train = pd.merge(x_train, ch_min, on=['channel'], how='left', sort=False)
#
#################################################################
x_train['5minute']=pd.DataFrame(columns=["5minute"])
x_train['5minute'].loc[(x_train['minute']>=0) & (x_train['minute']<5)]=0
x_train['5minute'].loc[(x_train['minute']>=5) & (x_train['minute']<10)]=1
x_train['5minute'].loc[(x_train['minute']>=10) & (x_train['minute']<15)]=2
x_train['5minute'].loc[(x_train['minute']>=15) & (x_train['minute']<20)]=3
x_train['5minute'].loc[(x_train['minute']>=20) & (x_train['minute']<25)]=4
x_train['5minute'].loc[(x_train['minute']>=25) & (x_train['minute']<30)]=5
x_train['5minute'].loc[(x_train['minute']>=30) & (x_train['minute']<35)]=6
x_train['5minute'].loc[(x_train['minute']>=35) & (x_train['minute']<40)]=7
x_train['5minute'].loc[(x_train['minute']>=40) & (x_train['minute']<45)]=8
x_train['5minute'].loc[(x_train['minute']>=45) & (x_train['minute']<50)]=9
x_train['5minute'].loc[(x_train['minute']>=50) & (x_train['minute']<55)]=10
x_train['5minute'].loc[(x_train['minute']>=55) & (x_train['minute']<=60)]=11
# number of clicks per 5minute for each channel
ch_5min=x_train.groupby(['channel','day','hour','5minute']).size().reset_index()
ch_5min.columns = ['channel','day','hour','5minute', 'channels_per_5min']
ch_5min=ch_5min.groupby(['channel']).max().reset_index()
ch_5min=ch_5min.drop(['day','hour','5minute'],axis=1)
x_train = pd.merge(x_train, ch_5min, on=['channel'], how='left', sort=False)
x_train=x_train.drop(['5minute'],axis=1)
# ####################################################################################
x_train['15minute']=pd.DataFrame(columns=["15minute"])
x_train['15minute'].loc[(x_train['minute']>=0) & (x_train['minute']<15)]=0
x_train['15minute'].loc[(x_train['minute']>=15) & (x_train['minute']<30)]=1
x_train['15minute'].loc[(x_train['minute']>=30) & (x_train['minute']<45)]=2
x_train['15minute'].loc[(x_train['minute']>=45) & (x_train['minute']<60)]=3

# number of clicks per 15minute for each channel
ch_15min=x_train.groupby(['channel','day','hour','15minute']).size().reset_index()
ch_15min.columns = ['channel','day','hour','15minute', 'channels_per_15min']
ch_15min=ch_15min.groupby(['channel']).max().reset_index()
ch_15min=ch_15min.drop(['day','hour','15minute'],axis=1)
x_train = pd.merge(x_train, ch_15min, on=['channel'], how='left', sort=False)
x_train=x_train.drop(['15minute'],axis=1)
####################################################################################
# channel with other features

ch_ip=x_train.groupby(['ip','channel']).size().reset_index()
ch_ip.columns = ['ip','channel', 'channel_ip']
x_train = pd.merge(x_train, ch_ip, on=['ip','channel'], how='left', sort=False)

ch_app=x_train.groupby(['app','channel']).size().reset_index()
ch_app.columns = ['app','channel', 'channel_app']
x_train = pd.merge(x_train, ch_app, on=['app','channel'], how='left', sort=False)

ch_os=x_train.groupby(['os','channel']).size().reset_index()
ch_os.columns = ['os','channel', 'channel_os']
x_train = pd.merge(x_train, ch_os, on=['os','channel'], how='left', sort=False)

ch_device=x_train.groupby(['device','channel']).size().reset_index()
ch_device.columns = ['device','channel', 'channel_device']
x_train = pd.merge(x_train, ch_device, on=['device','channel'], how='left', sort=False)

x_train=x_train.drop(['month','day','hour','minute','second','ip','device'],axis=1)

print("training is running")

print(x_train)
m = boosting(x_train,y_train,x_train)
pickle.dump(m, open("ch_features.pkl", 'wb'))