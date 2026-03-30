## SU01 Chapter 2

## binomial model B(10,0.1)
# compute P(X=2)
dbinom(2, size=10, prob=0.1) 

# plot pmf for B(10,0.1)
x <- 0:20
plot(x, dbinom(x, size = 10, prob = 0.1), 
     ylab="Prob", main = "pmf for B(10,0.1)")


## Poisson model Poisson(12)
# compute P(X=4)
dpois(4, lambda=12)   

# plot pmf for Poisson(12)
x <- 0:20
plot(x, dpois(x, lambda=12), 
     ylab="Prob", main = "pmf for Poisson(12)")



## Normal model N(0,1)
# compute P(X<0.3)
pnorm(0.3, mean = 0, sd = 1)

# plot the cumulative distribution function 
x = seq(-4,4,by = 0.05)
plot(x,pnorm(x, mean = 0, sd = 1),ylab="CDF",main = "CDF for N(0,1)")
