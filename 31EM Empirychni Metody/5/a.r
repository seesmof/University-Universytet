library(tidyverse)
library(ggpubr)
library(rstatix)

PlantGrowth %>% sample_n_by(group,size=1)
PlantGrowth=PlantGrowth %>% reorder_levels(group,order=c('ctrl','trt1','trt2'))
PlantGrowth %>% group_by(group) %>% get_summary_stats(weight,type='common')
ggboxplot(PlantGrowth,x='group',y='weight')
res.kruskal=PlantGrowth %>% kruskal_test(weight~group)
res.kruskal