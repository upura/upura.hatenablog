# Data Import
df = read.csv("C:/Users/ishihara/Google ドライブ/_Files_/稗方研究室/161103DLH/Data/data.csv", header = F)
newdata = read.csv("C:/Users/ishihara/Google ドライブ/_Files_/稗方研究室/161103DLH/Data/new.csv", header = F)
correct = c(1,1,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,1)

# Library Import
library(mxnet)

precision = c()
recall = c()
f_value = c()
# Setting
train <- data.matrix(df)
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

num_round = 0
for (i in 1:100) {
  num_round = num_round + 500
  model <- mx.model.FeedForward.create(softmax, X=train.x, y=train.y, ctx=devices, num.round=num_round, array.batch.size=100, learning.rate=0.03, momentum=0.99,  eval.metric=mx.metric.accuracy, initializer=mx.init.uniform(0.5), array.layout = "rowmajor", epoch.end.callback=mx.callback.log.train.metric(100))
  preds <- predict(model, test, array.layout = "rowmajor")
  pred.label <- max.col(t(preds)) - 1
  
  # 精度
  res = table(correct, pred.label)
  precision = c(precision, res[4]/(res[2] + res[4]))
  recall = c(recall, res[4]/(res[3] + res[4]))
  # f_value = c(f_value, 2*precision*recall/(precision+recall))
}

