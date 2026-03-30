## Chapter 5 Examples

## normal approximation for Binomial distribution 

# define n and p 
n <- 200
p <- 0.05
# check np and n(1-p)
print(n*p)
print(n*(1-p))
# compute z score by applying continuity correction
print(n*p)
print(n*p*(1-p))
z = (11-0.5-n*p)/sqrt(n*p*(1-p))
print(round(z),4)
# compute P(X<11)
round(pnorm(z),4)


## normal approximation for Poisson distribution
# define mean for normal distribution 
mu = 40
# define variance for normal distribution 
var = 40
# compute z value by applying continuity correction
z=(35+0.5-mu)/sqrt(var)
print(round(z,4))
# compute probability P(X<=35)
round(pnorm(z),4)
