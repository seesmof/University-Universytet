library(datarium)
data("jobsatisfaction", package="datarium")
str(jobsatisfaction)

library(ggplot2)
ggplot(data=jobsatisfaction,aes(x=gender,y=score))+geom_boxplot(aes(fill=education_level))

require(doBy)
summaryBy(score~gender+education_level,data=jobsatisfaction,FUN=c(mean,sd,length))

plot.design(jobsatisfaction)

with(jobsatisfaction,interaction.plot(x.factor=education_level,trace.factor=gender,response=score))

# weightgain = score
# type = gender
# source = education_level

Model=lm(score~gender*education_level,data=jobsatisfaction)
summary(Model)
anova(Model)