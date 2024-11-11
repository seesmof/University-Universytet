library(HSAUR2)
data(weightgain)
str(weightgain)

library(ggplot2)
ggplot(data=weightgain,aes(x=type,y=weightgain))+geom_boxplot(aes(fill=source))

require(doBy)
summaryBy(weightgain~type+source,data=weightgain,FUN=c(mean,sd,length))

plot.design(weightgain)

with(weightgain,interaction.plot(x.factor=type,trace.factor=source,response=weightgain))

m1=aov(weightgain~source+type+source:type,data=weightgain)
summary(m1)

m2=lm(weightgain~type*source,data=weightgain)
summary(m2)
lm(formula=weightgain~type*source,data=weightgain)

anova(m2)

m3=lm(weightgain~source*type,data=weightgain)
anova(m3)

set.seed(333)
weightgain2=weightgain[-c(1:7,33:43),]
m4=lm(weightgain~type*source,data=weightgain2)
m5=lm(weightgain~source*type,data=weightgain2)
anova(m4)
anova(m5)

summary(m4)
summary(m5)

plot.design(weightgain2)