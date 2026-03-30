## Chapter 4 Examples

# define sample size
n = 5
# compute mean for sample total
mu_T = n*1005
# compute variance for sample total
var_T = n*3^2
# compute standard deviation for sample total
print(sqrt(var_T))
# compute variance for sample mean 
print(3^2/5)
# compute z value 
z=(1002-1005)/sqrt(1.8)
round(z,4)
# compute probability P(Z<z)
round(pnorm(z),4)

