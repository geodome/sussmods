## MTH220 SU02 Chapter 2

## CI for population mean

## 2.1 Example: normal population with known variance 

# define sample mean
mean = 64.3
# define population standard deviation
sigma = sqrt(225)
# define sample size 
n = 20
# define z value (95% CI)
z=1.96
# compute upper limit for the confidence interval 
round(mean+z*sigma/sqrt(n),4)
# compute lower limit for the confidence interval 
round(mean-z*sigma/sqrt(n),4)


## 2.2 Example: normal population with unknown variance 

# define sample data 
x = c(3.27,3.17,3.24,2.92,2.99)
# compute sample size 
n = length(x)
# compute sample mean 
mean = mean(x)
# compute sample standard deviation 
s = sd(x)
# define t value 
t = 2.776 
# or calculate t value 
qt(0.025,df=4,lower.tail = FALSE)
# compute upper limit for the confidence interval 
round(mean+t*s/sqrt(n),4)
# compute lower limit for the confidence interval 
round(mean-t*s/sqrt(n),4)


## 2.2 Example: normal population with unknown variance 

# define sample size 
n = 200
# define sample mean 
mean = 0.824
# define sample standard deviation 
s = 0.042
# compute t value 
qt(0.005,df=n-1,lower.tail = FALSE)
# define z value 
z = 2.58
# compute upper limit for the confidence interval 
round(mean+z*s/sqrt(n),4)
# compute lower limit for the confidence interval 
round(mean-z*s/sqrt(n),4)




## Exercise 


# define sample size 
n = 60
# define sample mean 
mean = 60139.7
# define sample standard deviation 
s = 3645.94
# define z value 
z = 1.96
# calculate z value
# qnorm((1-0.95)/2,lower.tail = FALSE)
# compute upper limit for the confidence interval 
mean+z*s/sqrt(n)
# compute lower limit for the confidence interval 
mean-z*s/sqrt(n)
