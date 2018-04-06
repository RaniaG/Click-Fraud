#clean environment 
rm(list=ls())
#display work items
ls()
library(rstudioapi) # load it

library(ggplot2)
library(hexbin)
library(RColorBrewer)
library(corrplot)


# the following line is for getting the path of your current open file
current_path <- getActiveDocumentContext()$path 
# The next line set the working directory to the relevant one:
setwd(dirname(current_path ))
# you can make sure you are in the right directory
print( getwd() )

df1<-read.csv("chunks/train-000.csv")  #11:57-11:58

colnames(df1)
dim(df1)

str(df1)

#------------------------------is attributed-----------------------------------------------
any(is.na(df1$is_attributed))
is_att<-df1$is_attributed
NROW(is_att)
is_att[is_att==""] <- NA
is_att <- na.omit(is_att)
any(is.na(is_att))
NROW(is_att)  # no NA or blank

table(df1$is_attributed)

#----------------------------------click time----------------------------------------------

click_time<-df1$click_time


any(is.na(click_time))
NROW(click_time)
click_time[click_time==""] <- NA
any(is.na(click_time))
click_time <- na.omit(click_time)
NROW(click_time) #doesnt have NA or blank



df2<-df1
df2$click_time<-as.numeric(df2$click_time)


#class 0
c0<-df2[which(df2$is_attributed==0),]
c1<-df2[which(df2$is_attributed==1),]
d0 <- density(c0$click_time) 
d1 <- density(c1$click_time) 
plot(d0,main="distribution of click time in class 0 (red),class1(blue) " ,col="red")

lines(d1,col="blue")




#------------------------------------ip address--------------------------------
plot(density(c0$ip),main="plot dist of ip in class 0 (red) class 1(blue)",col="red")
lines(density(c1$ip),col="blue")


#--------------------------------app id------------------------------------
plot(density(c0$app),main="plot dist of app in class 0 (red) class 1(blue)",col="red")
lines(density(c1$app),col="blue")


#--------------------------------device------------------------------------
plot(density(c0$device),main="plot dist of device in class 0 (red) class 1(blue)",col="red")
lines(density(c1$device),col="blue")

#--------------------------------os------------------------------------
plot(density(c0$os),main="plot dist of os in class 0 (red) class 1(blue)",col="red")
lines(density(c1$os),col="blue")

#--------------------------------channel------------------------------------
plot(density(c0$channel),main="plot dist of channel in class 0 (red) class 1(blue)",col="red")
lines(density(c1$channel),col="blue")


#---------------------correlations-----------------------------------
df2$attributed_time<-as.numeric(df2$attributed_time)
class(df2$attributed_time)
corrM <- cor(df2)
corrplot(corrM, method = "square")
corrplot(corrM, method = "number")

#-------------------------------attributed time-------------------------------------------


att_time<-df1$attributed_time

att_time[att_time==""] <- NA
any(is.na(att_time))
att_time <- na.omit(att_time)


any(is.na(att_time)) #blank and NA omitted



NROW(att_time)



att_t<-df1[which(df1$attributed_time!=""),]
table(att_t$is_attributed)


