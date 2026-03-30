## SU04 Chapter3 

# define sample size 
n1 = n2 = 200
# compute point estimate 
p1 = 20/n1
p2 = 14/n2
p = (20+14)/(n1+n2)
# compute z test statistic 
z = (p1-p2)/sqrt(p*(1-p)*(1/n1+1/n2))
print(round(z,2))
# compute critical value 
qnorm(0.025,lower.tail = FALSE)

# 95% CI
(p1-p2)+qnorm(0.025,lower.tail = FALSE)*sqrt(p*(1-p)*(1/n1+1/n2))
(p1-p2)-qnorm(0.025,lower.tail = FALSE)*sqrt(p*(1-p)*(1/n1+1/n2))
