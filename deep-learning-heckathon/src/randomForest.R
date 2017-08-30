# Data Import
df = read.csv("C:/Users/user/OneDrive/ドキュメント/WorkSpace/data.csv", header = F)
newdata = read.csv("C:/Users/ishihara/Google ドライブ/_Files_/稗方研究室/161103DLH/Data/new.csv", header = F)

library(randomForest)
tuneRF(df[,-1],df[,1],doBest=T)
xorc.rf<-randomForest(df[,1]~., df[,-1], mtry = 2)
out.rf<-predict(xorc.rf,newdata=newdata[,2:29])

plot(out.rf)
abline(h=0.5, col="red")

result_test = data.frame(newdata[,1])
result_test$result_value = out.rf
write.csv(result_test, "C:/Users/user/OneDrive/ドキュメント/WorkSpace/r.csv")
