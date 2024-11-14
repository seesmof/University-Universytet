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

jobsatisfaction %>% kruskal_effsize(score~education_level)

pwc=jobsatisfaction %>% dunn_test(score~education_level,p.adjust.method='bonferroni')

pwc

pwc2=jobsatisfaction %>% wilcox_test(score~education_level,p.adjust.method='bonferroni')

pwc2

pwc=pwc %>% add_xy_position(x='education_level')

ggboxplot(jobsatisfaction,x='education_level',y='score')+stat_pvalue_manual(pwc,hide.ns=T)+labs(subtitle=get_test_label(res.kruskal,detailed=T),caption=get_pwc_label(pwc))