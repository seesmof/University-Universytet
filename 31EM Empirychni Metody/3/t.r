library(HSAUR2)
data(weightgain)
str(weightgain)

library(ggplot2)
ggplot(data=weightgain,aes(x=type,y=weightgain))