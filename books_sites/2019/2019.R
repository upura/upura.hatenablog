library(primes)
x = generate_primes(max = 40)
x = append(x, c(1))
df = combn(x, m=3)
table(apply(df, 2, function(x) {return (sum(x^2))}))

y = c(17, 19, 37)
sum(y^2)

z = c(11, 23, 37)
sum(z^2)

apply(expand.grid(x, x, x), 1, function(x) {return (sum(x^2))})
