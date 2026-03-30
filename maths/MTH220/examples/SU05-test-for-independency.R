
## SU5 Chapter2 Test for independency 

# define table 
table1 = rbind(c(63, 42, 15), c(58, 61, 31), c(14, 47, 29))
colnames(table1) = c("MATH Low","MATH Average", "MATH High")
rownames(table1) = c("STATS Low","STATS Average", "STATS High")
table1
# perform chi-square test 
chisq.test(table1)



# define table 
table = cbind(c(3,10), c(12,5))
rownames(table) = c("Treatment","Placebo")
colnames(table) = c("Jet lag","No jet lag")
table
# perform chi-square test 
chisq.test(table, correct = FALSE)
