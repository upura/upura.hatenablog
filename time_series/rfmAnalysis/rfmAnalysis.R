hist(df$recency, main="Histogram of Recency", xlab="recency")
hist(log10(df$frequency), main="Histogram of Log10(Frequency)", xlab="log10(frecency)")
hist(log10(df$monetary), main="Histogram of Log10(Monetary)", xlab="log10(monetary)")