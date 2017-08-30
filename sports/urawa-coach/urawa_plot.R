data <- read.csv("C:\\urawa.csv", row.names = 1)
library(ggplot2)
library("ggrepel")

g <- ggplot(
  data,
  aes (
    x = data[,1],
    y = data[,2],
    colour = data[,3],
    label = rownames(data)
  )
)

g <- g +  geom_point(
  size = 3
)

g <- g + geom_text_repel()
g <- g + xlab("Goal For per Game")
g <- g + ylab("Goal Against per Game")

plot(g)