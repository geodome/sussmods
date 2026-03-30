## SU04 Chapter4

##  mean diff (matched pairs)

# define samples 
B = c(49,57,60,39,42,48,52,
      51,47,45,39,49,47,59)
A = c(54,64,60,48,45,50,58,
      53,48,55,40,56,49,64)
# compute sample difference 
D = A-B
# compute mean for sample difference 
mean_D = mean(D)
# compute standard deviation for sample difference 
sd_D = sd(D)
# compute test statistic 
t = (mean_D-3.1)/(sd_D/sqrt(14))
print(round(t,2))
# compute critical value 
qt(0.05,df=13,lower.tail = FALSE)

# perform t-test 
t.test(A-B,alternative = "greater",mu=3.1,conf.level=0.95)
