library(HSAUR2)
data(weightgain)
str(weightgain)

library(ggplot2)
ggplot(data=weightgain,aes(x=type,y=weightgain))+geom_boxplot(aes(fill=source))

m1=aov(weightgain~source+type+source:type,data=weightgain)
summary(m1)