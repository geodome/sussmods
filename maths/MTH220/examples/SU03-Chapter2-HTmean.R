
## SU03 Chapter2 

## test on normal population mean with known variance 

# define sample size 
n = 25
# define sample mean 
mean = 8.091
# define population standard deviation 
sigma = 0.16
# define \mu_0 
mu0 = 8
# compute z test statistics 
z = (mean-mu0)/(sigma/sqrt(n))
print(round(z,2))

# compute critical values 
round(qnorm(0.005,lower.tail = FALSE),2)


## test on normal population mean with unknown variance 

# define sample size 
n = 40
# define sample mean 
mean = 5.5
# define sample standard deviation 
s = 1.2
# define \mu_0 
mu0 = 5
# compute t test statistics 
t = (mean-mu0)/(s/sqrt(n))
print(round(t,2))

# compute critical value
round(qt(0.01,df=39,lower.tail = FALSE),2)


## test on population mean with unknown population distribution

# define sample size 
n = 60
# define sample mean 
mean = 119.2
# define sample standard deviation 
s = 1
# define \mu_0 
mu0 = 120
# compute z test statistics 
z = (mean-mu0)/(s/sqrt(n))
print(round(z,2))

# compute critical value
round(qnorm(0.025,lower.tail = FALSE),2)



# define sample data 
x = c(171.6,191.8,178.3,184.9, 189.1)
# perform t test 
t.test(x,mu=185,alternative="less",conf.level = 0.95)

# calculate t test statistics 
t = (mean(x)-185)/(sd(x)/sqrt(length(x)))
print(t)
