
## SU06 Chapter1 

## Pearson Corelation

# define data
x = c(125.3, 98.2, 201.4, 147.3, 145.9,
      124.7, 112.2, 120.2, 161.2, 178.9)

y = c(77.9, 76.8, 81.5, 79.8, 78.2,
      78.3, 77.5, 77.0, 80.1, 80.2)

# scatter plot 
plot(x,y,xlab="Filtration rate",ylab="Moisture")

# compute pearson correlation
var(x,y)/(sd(x)*sd(y))

# calculate pearson correlation using R function
cor(x,y)

## Spearmen Rank Correlation 

x = c(8,5,11,13,10,5,18,15,2,8)

y = c(56,44,79,72,70,54,94,85,33,65)

# scatter plot 
plot(x,y,xlab="Hours studied",ylab="Scores")

# get rank 
xr = rank(x)
xr
yr = rank(y)
yr

# compute Spearmen Rank Correlation
cor(xr,yr)

cor(rank(-x),rank(-y))
