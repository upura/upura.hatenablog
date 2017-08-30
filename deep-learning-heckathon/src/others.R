# Data Import
df = read.csv("C:/Users/ishihara/Google ドライブ/_Files_/稗方研究室/161103DLH/Data/data.csv", header = F)

# Data Edit

df.pca = prcomp(df[,2:29], scale=T)
color = c("red", "blue")
plot(df.pca$x[1:2420,1], df.pca$x[1:2420,2])

library(scatterplot3d)
scatterplot3d(df.pca$x[,1:3], pch = 1)

plot(0, 0, type = "n", xlim = c(min(df.pca$x[,1]), max(df.pca$x[,1])), ylim = c(min(df.pca$x[,2]), max(df.pca$x[,2])),xlab = "x", ylab = "y")
points(df.pca$x[1:2473, 1], df.pca$x[1:2473, 2], col = "blue", pch = 1) #lose
points(df.pca$x[2474:4967, 1], df.pca$x[2474:4967, 2], col = "red", pch = 1) #win


barplot(summary(df.pca)$importance[2,])

library(rpart)

#決定木の分析の実行
data.rp <- rpart(V1~V2+V3+V4+V5+V6+V7+V8+V9+V10+V11+V12+V13+V14+V15+V16+V17+V18+V19+V20+V21+V22+V23+V24+V25+V26+V27+V28+V29,data=df,cp=0.01)
#結果の表示
print(data.rp)
#決定木のプロット
plot(data.match.central.rp,branch=0.6,margin=0.05)
data.rp

require(rpart.plot)
rpart.plot(data.rp)

require(useful)
income1 = glm(V1~V2+V3+V4+V5+V6+V7+V8+V9+V10+V11+V12+V13+V14+V15+V16+V17+V18+V19+V20+V21+V22+V23+V24+V25+V26+V27+V28+V29,data=df, family = binomial(link = "logit"))
summary(income1)
predict(df[,2:29])

result_predict = predict(income1, newdata=newdata[,-1])
library(caret)
titanic.glm <- train(
  data = df,
  V1~V2+V3+V4+V5+V6+V7+V8+V9+V10+V11+V12+V13+V14+V15+V16+V17+V18+V19+V20+V21+V22+V23+V24+V25+V26+V27+V28+V29,
  method = "glm",
  family = binomial())
result_predict2 = predict(titanic.glm, newdata=newdata[,-1])

library(randomForest)
xorc.rf<-randomForest(df[,1]~.,df[,2:29])
out.rf<-predict(xorc.rf,newdata=df[,2:29])

plot(out.rf)

library(e1071)
xorc.svm.rbf<-svm(df[,1]~.,df[,2:29], scale=F)
out.svm.rbf<-predict(xorc.svm.rbf,newdata=newdata[,-1])
plot(out.svm.rbf)

library(xgboost)
library(Matrix)
dtrain.mx <- sparse.model.matrix(df[,1]~.,df[,2:29])
dtest.mx <- sparse.model.matrix(~., newdata[,-1])
dtrain <- xgb.DMatrix(dtrain.mx, label = as.numeric(df[,1]))
dtest <- xgb.DMatrix(dtest.mx)
xorc.gdbt <- xgb.train(params=list(objective='binary:logistic'), data=dtrain, nrounds=25)
out.gdbt <- predict(xorc.gdbt, newdata=dtest)
plot(out.gdbt)


install.packages("drat", repos="https://cran.rstudio.com")
drat:::addRepo("dmlc")
install.packages("mxnet")
library(mxnet)

train<-data.matrix(df)
train.x<-train[,-1]
train.y<-as.numeric(train[,1])
test<-data.matrix(newdata[,-1])
data <- mx.symbol.Variable("data")
fc1 <- mx.symbol.FullyConnected(data, name="fc1", num_hidden=28)
act1 <- mx.symbol.Activation(fc1, name="tanh1", act_type="tanh")
fc2 <- mx.symbol.FullyConnected(act1, name="fc2", num_hidden=14)
act2 <- mx.symbol.Activation(fc2, name="tanh2", act_type="tanh")
fc3 <- mx.symbol.FullyConnected(act2, name="fc3", num_hidden=10)
act3 <- mx.symbol.Activation(fc3, name="tanh3", act_type="tanh")
fc4 <- mx.symbol.FullyConnected(act3, name="fc4", num_hidden=2)
softmax <- mx.symbol.SoftmaxOutput(fc4, name="softmax")
devices <- mx.cpu()
mx.set.seed(71)
model <- mx.model.FeedForward.create(softmax, X=train.x, y=train.y, ctx=devices, num.round=4000, array.batch.size=100, learning.rate=0.03, momentum=0.99,  eval.metric=mx.metric.accuracy, initializer=mx.init.uniform(0.5), array.layout = "rowmajor", epoch.end.callback=mx.callback.log.train.metric(100))
preds <- predict(model, test, array.layout = "rowmajor")
pred.label <- max.col(t(preds)) - 1
table(pred.label)
