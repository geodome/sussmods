# 1. A two-sample t test is carried out using two samples, each with sample 
# size n = 7, to compare two treatment conditions. The t statistic for this 
# study will have degrees of freedom equal to _______

n <- 7

cat("1. df = ", n + n - 2, "\n")

# 2. What is the pooled variance for the following two samples?
# Sample 1: n = 6 and SS = 56
# Sample 2: n = 4 and SS = 40

n1 <- 6; SS1 <- 56
n2 <- 4; SS2 <- 40

cat("2. pooled variance =", (SS1 + SS2)/(n1 + n2 - 2), "\n")

# An educational psychologist studies the effect of frequent testing on 
# retention of knowledge learnt in class. In one of the professor’s sections, 
# students are given quizzes each week. The second section receives only two 
# tests during the semester. At the end of the semester, both sections took the 
# same examination and the scores are summarized in the table below. A 
# two-tailed two-sample t test is carried out at 1% level of significance. 

n1 <- 15; mu1 <- 72; s1 <- sqrt(8)
n2 <- 15; mu2 <- 68; s2 <- sqrt(7)
df <- n1 + n2 - 2
alpha <- 0.01

# 4. Compute the pooled variance.
s <- sqrt(((n1 - 1)*s1^2 + (n2  - 1)*s2^2)/df)

cat("4. Pooled Variance =", s^2, "\n")

# 5. Compute the t(critical) value.

cat("5. t_critical =", qt(1 - alpha/2, df), "\n")

# 6. What is the value of the computed test statistic?

t <- (mu1 - mu2)/(s*sqrt(1/n1 + 1/n2))

cat("5. t =", t, "\n")
