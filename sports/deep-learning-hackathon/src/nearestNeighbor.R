# Data Import
df = read.csv("../data/data.csv", header = F)
newdata = read.csv("../data/new.csv", header = F)

for (j in 1:20) {
  minus <- function(x) {return (x - newdata[j, -1])}
  result <- apply(df[, -1], 1, minus) 
  
  r = c()
  for (i in 1:4967) {
    r = c(r, sum(as.data.frame(result[i]) == 0))
  }
  print(df[which.max(r),1])
}

