#clean environment 
rm(list=ls())
#display work items
ls()
library(rstudioapi) # load it

library(ggplot2)
library(hexbin)
library(RColorBrewer)
library(bigmemory.sri)
library(bigmemory)
options(bigmemory.allow.dimnames=TRUE)
library(biganalytics)
library(bigtabulate)


# the following line is for getting the path of your current open file
current_path <- getActiveDocumentContext()$path 
# The next line set the working directory to the relevant one:
setwd(dirname(current_path ))
# you can make sure you are in the right directory
print( getwd() )


dfsample<-read.csv("train.csv",nrows=100000)
colnames(dfsample)

df.matrix <- read.big.matrix("train.csv")
colnames(df.matrix) = c("ip", "app","device","os","channel","click_time","attributed_time","is_attributed")

# Get the location of the pointer to df.matrix. 
desc <- describe(df.matrix)


str(df.matrix)
is.big.matrix(df.matrix)
dim(df.matrix)
summary(df.matrix)
colnames(df.matrix)
rownames(df.matrix)


att_time<-sub.big.matrix(df.matrix, firstRow = 1, lastRow = NULL, firstCol = 7,
               lastCol = 7)
dim(att_time)


is_att<-sub.big.matrix(df.matrix, firstRow = 1, lastRow = NULL, firstCol = 8,
                         lastCol = 8)

dim(is_att)

summary(att_time)
str(att_time)

dt = data.frame(is_att,att_time)
f<-factor(is_att)
levels(f)


#plot 
a=hexbin(is_att,att_time)
plot(a)

df = data.frame(n, s, b)
# save the location to disk to share the object .
dput(desc , file="tmp/df.desc")


#------------------------------new session--------------------------------------
# Read the pointer from disk .
shared.desc <- dget("tmp/df.desc")

# Attach to the pointer in RAM.
shared.bigobject <- attach.big.matrix(shared.desc)

