library(RMeCab)

setwd("C:/Users/") # 作業ディレクトリ
f = file("rawdata/nikkei.txt","r")

out <- file("output.txt", "w")

while (1){
  a = readLines(con=f, 1)
  if (length(a) <= 0){
    break
  }
  res = RMeCabC(a)
  writeLines(paste(res), out, sep=",")
  writeLines(paste(""), out, sep="\n")
}
close(out)