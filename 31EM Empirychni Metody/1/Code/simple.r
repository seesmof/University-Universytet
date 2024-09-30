mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x,ux)))]
}

v <- 19
n <- v * 10
m <- v
s <- v / 10

dataset <- rnorm(n, m, s)
dataset <- round(dataset)
hist(dataset, col="green")

frequency_table <- table(dataset)
mean_value <- mean(dataset)
median_value <- median(dataset)
mode_value <- mode(dataset)
qunatiles <- quantile(dataset)

qunatiles
mode_value
median_value
mean_value
frequency_table
dataset

write.table(dataset, "E:\\University\\31EM\\l1\\data.txt")