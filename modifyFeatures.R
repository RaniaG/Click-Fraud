#clean environment 
rm(list=ls())
#display work items
ls()
library(rstudioapi) # load it


library(ggplot2)
library(hexbin)

library(RColorBrewer)
library(corrplot)
library(lubridate)
library(tidyr)

# the following line is for getting the path of your current open file
current_path <- getActiveDocumentContext()$path 
# The next line set the working directory to the relevant one:
setwd(dirname(current_path ))
# you can make sure you are in the right directory
print( getwd() )

df1<-read.csv("chunks/train-009.csv")  #1:44-
colnames(df1)
class0<-df1[which(df1$is_attributed==0), ]
class1<-df1[which(df1$is_attributed==1), ]



ip<-intersect(class1$ip,class0$ip)
NROW(ip)



#separate into date and time
into<-c("date","time")
df2<-separate(df1, click_time, into, sep = " ",convert = FALSE,remove=FALSE)
colnames(df2)
head(df2)


#separate into year month day
into<-c("year","month","day")
df3<-separate(df2, date, into, sep = "-",convert = FALSE,remove=FALSE)
colnames(df3)
head(df3)

#separate into hour minute secondd
into<-c("hour","minute","second")
df4<-separate(df3, time, into, sep = ":",convert = FALSE,remove=FALSE)
colnames(df4)
head(df4)
dim(df4)

#remove click time and attributed time and device and os
keeps<-c("ip","app","channel","year","month","day","hour","minute","second","is_attributed")
df5<-df4[keeps]
colnames(df5)
dim(df5)
write.csv(df5,"modified/train9.csv",row.names = FALSE)
