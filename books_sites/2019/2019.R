library(primes)
is_prime(2019)

library(gmp)
factorize(2019)

17^2 + 19^2 + 37^2

x = generate_primes(max = 50)

library(gtools)
xcombn = combinations(length(x), 3, x, repeats.allowed=TRUE)

# xcombn = combn(x, m=3)
# expand.grid(x, x, x)

results = apply(
  xcombn, 1, function(x) {return (sum(x^2))}
)
tbl = table(results)

tbl

y = c(17, 19, 37)
sum(y^2)

z = c(11, 23, 37)
sum(z^2)
