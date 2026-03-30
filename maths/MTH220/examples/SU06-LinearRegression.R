
## SU06 Chapter1 


# define data
x = c(125.3, 98.2, 201.4, 147.3, 145.9,
      124.7, 112.2, 120.2, 161.2, 178.9)

y = c(77.9, 76.8, 81.5, 79.8, 78.2,
      78.3, 77.5, 77.0, 80.1, 80.2)

# scatter plot 
plot(x,y,xlab="Filtration rate",ylab="Moisture")

# compute SSxx
SSxx = sum((x-mean(x))^2)
SSxx

# compute SSxy
SSxy = sum((x-mean(x))*(y-mean(y)))
SSxy

# compute estimate of the slope (beta)
beta = SSxy/SSxx
round(beta,4)

# compute estimate of the intercept (alpha)
alpha = mean(y)-beta*mean(x)
round(alpha,4)

# plot the straight line 
h = seq(min(x),max(x),by=0.1)
yhat = round(alpha,4)+round(beta,4)*h
lines(h,yhat,col="red",lwd=2)

# Using R function 
lm(y~x)
