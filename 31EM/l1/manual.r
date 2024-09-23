v <- 19
n <- v * 10
m <- v
s <- v / 10

# generate dataset
dataset <- rnorm(n, m, s)

# save data into txt file 
write.table(dataset, "E:\\University\\31EM\\l1\\data.txt")

# get histogram
hist(dataset, col="green")


# get frequency table
frequency_table <- table(dataset)
# get mean
mean_value <- mean(dataset)
# get median
median_value <- median(dataset)
# get mode
mode_value <- mode(dataset)
# get qunatiles
qunatiles <- quantile(dataset)

# write data into rtf file
sink("E:\\University\\31EM\\l1\\stats.rtf")

frequency_table
mean_value
median_value
mode_value
qunatiles