library(RMeCab)

result <- RMeCabFreq("C:/Users/ishihara/Google ƒhƒ‰ƒCƒu/Workspace/nikkei.txt")
result = result[order(-result$Freq),]

result <- result[result[, 2] == "–¼ŽŒ" & result[, 3] == "ˆê”Ê" & result[, 4] > 50, ] 
k.col <- rainbow(nrow(result))
matplot(1:nrow(result), result[,4], type = "n", xlab="", ylab = "Frequancy")
for(i in 1:nrow(result)){
  matlines(i, result[i,4], type = "h", col = k.col[i],  lwd =5)
}
legend(8, max(result$Freq), legend = result$Term, col = k.col, lwd = 5)
