## SU04 Chapter1 

## mean diff with known variances 

# define sample means
mean1 = 175.4
mean2 = 168.6
# define population variances 
var1 = var2 = 1
# define sample sizes 
n1 = 10
n2 = 12
# compute test statistic 
z = (mean1-mean2-5)/sqrt(var1/n1+var2/n2)
print(round(z,2))

# compute critical value 
qnorm(0.05,lower.tail = FALSE)

# confidence interval 
(mean1-mean2)+qnorm(0.05,lower.tail = FALSE)*sqrt(var1/n1+var2/n2)
(mean1-mean2)-qnorm(0.05,lower.tail = FALSE)*sqrt(var1/n1+var2/n2)