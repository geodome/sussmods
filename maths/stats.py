from sympy import *
from sympy.stats import *
from typing import Callable 

number = int|float

# discrete uniform distribution
ddunif: Callable[[int,int], Rational] = lambda x,n: density(Die("",n))[x]
pdunif: Callable[[int,int], Rational] = lambda x,n: cdf(Die("",n))[x]
qdunif: Callable[[float,int], int] = lambda q,n: quantile(Die("",n))(q)

# continuous uniform distribution

dunif:Callable[[float, float, float], float] = lambda x,a,b: density(Uniform("",a,b))(x)
punif: Callable[[float,float,float], float]  = lambda x,a,b: cdf(Uniform("",a,b))(x)
qunif:Callable[[float,float,float], float]  = lambda q,a,b: quantile(Uniform("",a,b))(q)

# binomial distribution
dbinom: Callable[[int,int,float], float] = lambda x, n, p: density(Binomial("", n, p))(x)
pbinom: Callable[[int,int,float], float]= lambda x, n, p: cdf(Binomial("", n, p))[floor(x)]
qbinom: Callable[[float,int,float], float] = lambda q, n, p: quantile(Binomial("", n, p))(q)

# geometric distribution

# poisson distribution
# exponential distribution

# normal distribution
pnorm: Callable[[float,float,float], float] = lambda x, mu, sigma: cdf(Normal("", mu, sigma))(x)
qnorm: Callable[[float, float, float], float] = lambda p, mu, sigma: quantile(Normal("", mu, sigma))(p)