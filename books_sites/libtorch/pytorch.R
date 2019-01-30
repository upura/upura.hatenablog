# install.packages("devtools")

Sys.setenv(TORCH_HOME="/libtorch")
devtools::install_github("dfalbel/torch")


library(torch)
x <- array(runif(8), dim = c(2, 2, 2))
y <- tensor(x)
y