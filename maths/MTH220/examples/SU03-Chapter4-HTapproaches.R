
## SU03 Chapter4

## test using p-value 

# define sample mean
mean = 8.112
# define mu_0
mu_0 = 8
# define population standard deviation
sigma = 0.16
# define sample size 
n = 15
# compute test statistic 
z = (mean-mu_0)/(sigma/sqrt(n))
# compute p value 
p = 2*(1-pnorm(z))
print(p)


## test using CI

# define sample mean
mean = 1570
# define sample standard deviation
s = 120
# define sample size 
n = 100
# define z value 
z=2.58
# compute upper limit for the confidence interval 
mean+z*s/sqrt(n)
# compute lower limit for the confidence interval 
mean-z*s/sqrt(n)
