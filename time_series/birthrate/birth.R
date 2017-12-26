label <- t(df['year'])
num <- t(df['birth_num'])
rate <- t(df['birth_rate'])

par(mar=c(4, 5, 2, 5))
barx <- barplot(num, names.arg=label, xlab = "", ylab = "Number of live births", col=c('white'))

par(new=T)
plot(barx, as.matrix(rate), type="o", axes = F, xlab = "", ylab = "")
axis(side = 4)
mtext("Birthrate", side = 4, line = 3)
box()

abline(v=51)
