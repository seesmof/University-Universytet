library(tidyverse)
library(ggpubr)
library(rstatix)

PlantGrowth %>% sample_n_by(group,size=1)
PlantGrowth=PlantGrowth %>% reorder_levels(group,order=c('ctrl','trt1','trt2'))
PlantGrowth %>% group_by(group) %>% get_summary_stats(weight,type='common')
ggboxplot(PlantGrowth,x='group',y='weight')
res.kruskal=PlantGrowth %>% kruskal_test(weight~group)
res.kruskal
PlantGrowth %>% kruskal_effsize(weight~group)
pwc=PlantGrowth %>% dunn_test(weight~group,p.adjust.method='bonferroni')
pwc
pwc2=PlantGrowth %>% wilcox_test(weight~group,p.adjust.method='bonferroni')
pwc2
pwc=pwc %>% add_xy_position(x='group')
ggboxplot(PlantGrowth,x='group',y='weight')+stat_pvalue_manual(pwc,hide.ns=T)+labs(subtitle=get_test_label(res.kruskal,detailed=T),caption=get_pwc_label(pwc))