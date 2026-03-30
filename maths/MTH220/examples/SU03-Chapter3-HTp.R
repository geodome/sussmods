
## SU03 Chapter3

## test on population proportion p 

# compute p_hat 
p_hat = 10/500
# define p_0
p_0 = 0.03
# define sample size 
n = 500
# compute z test statistics 
z = (p_hat-p_0)/sqrt(p_0*(1-p_0)/n)
print(round(z,2))
# compute critical values
qnorm(0.05,lower.tail = FALSE)
