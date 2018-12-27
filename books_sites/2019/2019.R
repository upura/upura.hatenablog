is_prime(2019)

library(gmp)
factorize(2019)

17^2 + 19^2 + 37^2

library(primes)
x = generate_primes(max = 40)
xcombn = combn(x, m=3)
results = apply(
  xcombn, 2, function(x) {return (sum(x^2))}
)
table(results)

y = c(17, 19, 37)
sum(y^2)

z = c(11, 23, 37)
sum(z^2)
