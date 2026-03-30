# Samples of size n = 9 are selected from a population with mean µ = 60 and 
# standard deviation σ = 12. 

n <- 9
sigma <- 12
mu <- 60

# 1. What is the expected value for the distribution of sample means?

cat("1. sample mean =", mu, "\n")

# 2. What is the standard deviation for the distribution of sample means?

cat("2. sample sd =", sigma/sqrt(n), "\n")


# 3. The mean rent of an apartment is $780.  You randomly select 9 apartments. 
# Compute the probability that the mean rent is less than $825.  Assume that 
# the rents are normally distributed with a mean of $780 and a standard 
# deviation of $150.

n <- 9
mu <- 780
sigma <- 150

cat("3. P(rent < 825) =", pnorm(825, mu, sigma/sqrt(n)), "\n")

# 4. A bank found that 24% of it’s loans become delinquent. Suppose 200 loans 
# are made. Using normal approximation to binomial model, compute the approximate 
# probability that at least 60 loans are delinquent.

p <- 0.24
n <- 200

# P(at least 60 delinquent loans) = P(60 delinquent loans) + P(>60 delinquent loans)
p_60 <- dbinom(60, 200, p)
p_le60 <- pnorm(60 + 0.5, n*p, sqrt(n*p*(1-p)))
p_gt60 <- 1 - p_le60

cat("4. P(at least 60 deliquent loans) = ", p_60 + p_gt60, "\n")

# 5. Given that the distribution of PaO2 levels among newborns follows a normal 
# distribution with mean = 38 and a standard deviation = 9. Suppose we take a 
# sample of size n = 25. Compute the probability that the sample average will 
# be greater than 36.

mu <- 38
sigma <- 9
n <- 25

cat("5. P(sample average > 36) = 1 - P(sample average <= 36) =", 1- pnorm(36, mu, sigma/sqrt(n)), "\n")

# 6. A random sample of n = 16 has sample mean = 40 and sample variance = 36.  
# Construct a 95% confidence interval (i.e. t interval) for μ.

# population variance unknown, so use t-distribution

n <- 16
mu <- 40
s <-  sqrt(36)
alpha <- 0.5
delta <- qt(1 - alpha/2, n-1) * s/sqrt(n)

cat("8. 95% confidence interval = (", mu - delta, ",", mu + delta, ")\n")
  
# 9. A random sample of 9 power supply was drawn from a normal population.  
# The mean voltage is found to be 5.3 volts. From past historical testing, the 
# population standard deviation is known to be 0.4.  Construct a 90% confidence 
# interval for the population mean voltage.

n <- 9
sigma <- 0.4
sample_mean <- 5.3
alpha <- 1 - 0.9
delta <- qnorm(1 - alpha/2)*sigma/sqrt(n)

cat("9. confidence interval = (", sample_mean - delta, ",", sample_mean + delta,")\n")