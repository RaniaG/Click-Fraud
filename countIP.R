#count ip in time ignoring other features

#clean environment 
rm(list=ls())
#display work items
ls()
library(rstudioapi) # load it

library(ggplot2)
library(hexbin)
library(RColorBrewer)
library(corrplot)
library(plyr)

# the following line is for getting the path of your current open file
current_path <- getActiveDocumentContext()$path 
# The next line set the working directory to the relevant one:
setwd(dirname(current_path ))
# you can make sure you are in the right directory
print( getwd() )
df<- read.csv("modified/train0.csv")

class(df$second)

keeps<-c("ip","hour","day","month","year","is_attributed")
dftemp<-df[keeps]


ip_hourly<-count(dftemp,vars=c("ip","hour","day","month","year"))
head(ip_hourly)

