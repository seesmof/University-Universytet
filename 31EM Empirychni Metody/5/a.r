library(tidyverse)
library(ggpubr)
library(rstatix)

PlantGrowth %>% sample_n_by(group,size=1)