## SU04 Chapter2

## mean diff with unknown variances 

# define sample data 
girls = c(52,65,48,58,53,53,67,56,70)
boys = c(50,48,60,45,53,58,40,38)
# compute sample means 
mean_g = mean(girls)
mean_b = mean(boys)
# compute sample variance s
var_g = var(girls)
var_b = var(boys)
# compute sample sizes
n_g = length(girls)
n_b = length(boys)
# compute sample variance
s_p2=((n_g-1)*var_g+(n_b-1)*var_b)/(n_g+n_b-2)
# compute test statistic
t = (mean_g-mean_b)/sqrt(s_p2*(1/n_g+1/n_b))
print(round(t,2))
# critical value 
qt(0.05,df=15,lower.tail = FALSE)
# compute p value 
pt(t,df=15,lower.tail = FALSE)

# perform t-test 
t.test(girls,boys,alternative = "greater",mu=0,var.equal=TRUE,conf.level=0.95)

