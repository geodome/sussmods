
## SU5 Chapter 2 Goodness-of-fit test 

# define errors 
x = c(0:9)
print(x)
# define observed frequencies
O = c(18,53,103,107,82,46,18,10,2,1)
# estimate lambda 
lambda = round(sum(x*O/sum(O)))
# compute poisson probability for x: P(X<=x) 
Fx = ppois(x, lambda=3) 
print(round(Fx,4))
px = round(c(Fx[1],diff(Fx)),4)
print(px)
# compute expected frequencies 
E = sum(O)*px
print(round(E,2))
# combined frequencies 
E_new = c(E[1:7],sum(E[8:10]))
O_new = c(O[1:7],sum(O[8:10]))
round((E_new-O_new)^2/E_new,4)
# compute test statistic 
w = sum((E_new-O_new)^2/E_new)
print(w,4)
