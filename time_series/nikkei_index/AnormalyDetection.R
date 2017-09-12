library(AnomalyDetection)
df = read.csv("nikkei_index.csv")
data = data.frame(as.POSIXlt(df[,1]),df[,4])
plot(data, xlab = "date", ylab = "ending price")
res <- AnomalyDetectionTs(data, max_anoms=0.02, direction='both', plot=TRUE)
res