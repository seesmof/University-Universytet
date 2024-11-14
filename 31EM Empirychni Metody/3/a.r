library(datarium)
data("jobsatisfaction", package="datarium")
str(jobsatisfaction)

library(ggplot2)
ggplot(data=jobsatisfaction,aes(x=gender,y=score))+geom_boxplot(aes(fill=education_level))