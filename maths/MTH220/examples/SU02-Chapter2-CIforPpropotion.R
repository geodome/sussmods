## MTH220 SU02 Chapter 3

## CI for population proportion p



## Example: 

# define sample size 
n = 500
# compute point estimator for p 
p_hat = 421/n
# define z value 
z = 1.96 
# compute upper limit for the confidence interval 
round(p_hat+z*sqrt(p_hat*(1-p_hat)/n),4)
# compute lower limit for the confidence interval 
round(p_hat-z*sqrt(p_hat*(1-p_hat)/n),4)
