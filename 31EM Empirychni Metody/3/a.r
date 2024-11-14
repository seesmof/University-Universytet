library(datarium)
data("jobsatisfaction", package="datarium")
str(jobsatisfaction)

library(ggplot2)
ggplot(data=jobsatisfaction,aes(x=gender,y=score))+geom_boxplot(aes(fill=education_level))

require(doBy)
summaryBy(score~gender+education_level,data=jobsatisfaction,FUN=c(mean,sd,length))