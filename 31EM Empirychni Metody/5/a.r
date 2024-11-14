library(tidyverse)
library(ggpubr)
library(rstatix)
library(datarium)
data('jobsatisfaction',package='datarium')


jobsatisfaction %>% sample_n_by(education_level,size=1)

# jobsatisfaction=jobsatisfaction %>% reorder_levels(group,order=c('ctrl','trt1','trt2'))

jobsatisfaction %>% group_by(education_level) %>% get_summary_stats(score,type='common')

ggboxplot(jobsatisfaction,x='education_level',y='score')

res.kruskal=jobsatisfaction %>% kruskal_test(score~education_level)

res.kruskal

PlantGrowth %>% kruskal_effsize(weight~group)

pwc=PlantGrowth %>% dunn_test(weight~group,p.adjust.method='bonferroni')

pwc

pwc2=PlantGrowth %>% wilcox_test(weight~group,p.adjust.method='bonferroni')

pwc2

pwc=pwc %>% add_xy_position(x='group')

ggboxplot(PlantGrowth,x='group',y='weight')+stat_pvalue_manual(pwc,hide.ns=T)+labs(subtitle=get_test_label(res.kruskal,detailed=T),caption=get_pwc_label(pwc))