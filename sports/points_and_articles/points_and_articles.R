df = read.csv("C:/points_and_articles.csv")

# with legend
library(ggplot2)
library("ggrepel")

g <- ggplot(
  df,
  aes (
    x = df[,3],
    y = df[,4],
    label = df[,2]
  )
)

g <- g +  geom_point(
  size = 3
)

g <- g + geom_text_repel()
g <- g + xlab("points")
g <- g + ylab("number of articles")

plot(g)

# lm
plot(df[,4] ~ df[,3], xlab = "points", ylab = "number of articles")
result <- lm(df[,4] ~ df[,3])
abline(result)
summary(result)  
