# Follow Google Style Guide for R
# https://web.stanford.edu/class/cs109l/unrestricted/resources/google-style.html

# In MTH219 the p percentile is calculated as (p/100)*(n+1) -th term
# R's quantile() implementation of the percentile calculation is different
# Hence, need to implement a separate percentile function solely for MTH219 use
Percentile <- function(data, p) {
  sorted <- sort(data)
  percentiles <- p

  i <- 0
  for (p0 in p) {
    i <- i + 1

    index <- min(length(sorted), max(1, (p0/100) * (length(data) + 1)))

    if (is.integer(index)) {
      percentiles[i] <- sorted[index]
      next
    }

    index0 <- floor(index)
    index1 <- ceiling(index)
    delta <- (index -  index0) * (sorted[index1] - sorted[index0])
    percentiles[i] <- sorted[index0] + delta
  }

  return(data.frame(Percentile=p, Value=percentiles))
}

# R has no native implementation to extract the mode of a data set.
Mode <- function(data) {
  tab <- table(data)
  max.freq <- max(tab)
  modes <- tab[tab == max.freq]
  return(names(modes))
}

# coefficient of variation
CV <- function(data) sd(data)/mean(data)

# Methods for Handling Probability Table
ProbTable.Create <- function(x, px) rbind(x, px)
ProbTable.Mean <- function(ptable) sum(ptable[1,] * ptable[2,])
ProbTable.StdDev <- function(ptable) sqrt(ProbTable.Var(ptable))
ProbTable.Var <- function(ptable) sum(ptable[2,] * (ptable[1,] - ProbTable.Mean(ptable))^2)

UPPER <- 0
LOWER <- 1
TWOSIDED <-2

# One Sample Z Test

OneSample.Z <- function(t, mu, sigma, n) (t - mu)/(sigma/sqrt(n))

OneSample.Z_critical <- function(alpha, tail, sigma, n) {
  if(tail == UPPER) {
    return(qnorm(1-alpha, mu, sigma/sqrt(n)))
  }
  if(tail == LOWER) {
    return(qnorm(alpha, mu, sigma/sqrt(n)))
  }
  if(tail == TWOSIDED) {
    return(qnorm(1-alpha/2, mu, sigma/sqrt(n)))
  }
  print("Invalid tail")
}

# One Sample T Test

OneSample.T <- function(t, mu, sigma, n) OneSample.Z(t, mu, sigma, n)

OneSample.T_critical <- function(alpha, tail, n) {
  if(tail == UPPER) {
    return(qt(1-alpha, n-1))
  }
  if(tail == LOWER) {
    return(qt(alpha, n-1))
  }
  if(tail == TWOSIDED) {
    return(qt(1-alpha/2, n-1))
  }
  print("Invalid tail")
}

OneSample.ConfidenceInterval <- function(mu, sigma, n, confidence, tail, pop_variance_known) {
  alpha = 1 - confidence
  cat("confidence level = ", confidence, "\nalpha =", alpha, "\n")
  cat("mu =", mu, "\n")
  s <- sigma/sqrt(n)
  cat("sigma/sqrt(n) =", s, "\n")
  if(pop_variance_known) {
    cat("Population variance known => Use normal distribution.\n")
    if(tail == UPPER) {
      z_critical <- qnorm(1-alpha)
      cat("z_critical = qnorm(1-alpha) =", z_critical, "\n")
      upper = mu + z_critical*s 
      cat("upper bound = mu + z_critical*sigma/sqrt(n) =", upper, "\n")
      cat("confidence interval: {x : x <", upper,"}\n")
    }
    if(tail == LOWER) {
      z_critical <- qnorm(alpha)
      cat("z_critical = qnorm(alpha) =", z_critical, "\n")
      lower <- mu - z_critical*s
      cat("lower bound = mu - z_critical*sigma/sqrt(n) =", lower, "\n")
      cat("confidence interval: {x: x >", qnorm(alpha, mu, sigma/sqrt(n)), "}\n")
    }
    if(tail == TWOSIDED) {
      z_critical = qnorm(1-alpha/2)
      cat("z_critical = qnorm(1 - alpha/2) =", z_critical, "\n")
      upper = mu + z_critical*s
      lower = mu - z_critical*s
      cat("upper bound = mu + z_critical*sigma/sqrt(n) =", upper, "\n")
      cat("lower bound = mu - z_critical*sigma/sqrt(n) =", lower, "\n")
      cat("confidence interval: ", "(", lower, ",", upper, ")\n")
    }
  } else {
    cat("Population variance unknown => Use T-Distribution with df", n-1, "\n")
    if(tail == UPPER) {
      t_c <- qt(confidence, n-1)
      cat("t_critical =", t_c, "\n")
      upper <- mu + t_c*s
      cat("upper bound = mu + t_critical*sigma/sqrt(n) =", upper, "\n")
      cat("confidence interval: {x: x <", upper, "}\n")
    }
    if(tail == LOWER) {
      t_c <- qt(alpha, n-1)
      cat("t_critical =", t_c, "\n")
      lower <- mu - t_c*s
      cat("lower bound = mu - t_critical*sigma/sqrt(n) =", lower, "\n")
      cat("confidence interval: {x: x >", lower, "}\n")
    }
    if(tail == TWOSIDED) {
      t_c <- qt(1-alpha/2, n-1)
      cat("t_critical = qnorm(1-alpha/2)", t_c, "\n")
      upper = mu + t_c * s
      lower = mu - t_c * s
      cat("upper bound = mu + t_critical*sigma/sqrt(n) =", upper, "\n")
      cat("lower bound = mu - t_critical*sigma/sqrt(n) =", lower, "\n")
      cat("confidence interval: ", "(", lower, ",", upper, ")\n")
    }
  }
}

# this method assumes normal distribution
OneSample.MinSampleSize <- function(confidence, sigma, ci_length) {
  alpha <- 1 - confidence
  z_critical <- qnorm(1-alpha/2)
  return (2*sigma*z_critical/ci_length)^2
}

# Two Sample Z Test

TwoSample.StdDev <- function(sigma1, n1, sigma2, n2) sqrt(sigma1^2/n1 + sigma2^2/n2)

TwoSample.Z <- function(mu1, sigma1, n1, mu2, sigma2, n2) (mu1 - mu2) / TwoSample.StdDev(sigma1, n1, sigma2, n2)

TwoSample.Z_critical <- function(alpha, tail) {
  if(tail == UPPER) {
    return(qnorm(1-alpha))
  }
  if(tail == LOWER) {
    return(qnorm(alpha))
  }
  if(tail == TWOSIDED) {
    return(qnorm(1-alpha/2))
  }
  print("Invalid tail")
}

# Two Sample T Test

TwoSample.PooledVar <- function(sd1, n1, sd2, n2) {
  numerator <- (n1 - 1)*sd1^2 + (n2 - 1)*sd2^2
  denominator <- n1 + n2 - 2
  return(numerator/denominator)
}

TwoSample.T <- function(mu1, sd1, n1, mu2, sd2, n2) {
  cat("mean_x1 = sum_x1/n1 = ")
  numerator <- mu1 - mu2
  sp <- TwoSample.PooledVar(sd1, n1, sd2, n2)
  cat("pooled variance sp = ((n1 - 1)*s1^2 + (n2 -1)*s2^2)/(n1 + n2 - 2) =", sp, "\n")
  denominator <- (sqrt(1/n1 + 1/n2)*sp)
  return(numerator/denominator)
}

TwoSample.T_critical <- function(alpha, tail, n1, n2) {
  if(tail == UPPER) {
    return(qt(1-alpha, n1 + n2 - 2))
  }
  if(tail == LOWER) {
    return(qt(alpha, n1 + n2 - 2))
  }
  if(tail == TWOSIDED) {
    return(qt(1-alpha/2, n1 + n2 -2))
  }
  print("Invalid tail")
}

# Pair Testing

PairTest.d <- function(x1, x2) (x1 - x2)

PairTest.Mean <- function(d) mean(d)

PairTest.Sd <- function(d) sd(d)

PairTest.Var <- function(d) var(d)

PairTest.T <- function(d) {
  t <- mean(d)
  sigma <- PairTest.Sd(d)
  n <- length(d)
  return (OneSample.T(t, 0, sigma, n))
}

PairTest.T_critical <- function(alpha, tail, n) OneSample.T_critical(alpha, tail, n)

# One-Way Anova

Anova.Test <- function(confidence, rmatrix) {
  nrow <- length(rmatrix[1,])
  ncol <- length(rmatrix[,1])
  cat("N =", length(rmatrix), "k =", nrow, "\n")
  grand_mean <- sum(rmatrix)/length(rmatrix)
  SST <- sum((rmatrix - grand_mean)^2)
  SSTR <- 0
  SSE <- 0
  group_mean <- NULL
  for(row in 1:nrow) {
    group <- rmatrix[row,]
    group_mean <- append(group_mean, mean(group))
    SSTR <- SSTR + length(group)*sum((mean(group) - grand_mean)^2)
    SSE <- SSE + sum((group - mean(group))^2)
  }
  SST_df <- length(rmatrix) - 1
  SSTR_df <- nrow - 1
  SSE_df <- length(rmatrix) - nrow
  cat("grand_mean =", grand_mean, "group_mean =", group_mean, "\n")
  cat("SST =", SST, "with df = N - 1 =", SST_df, "\n")
  cat("SSTR =", SSTR, "with df = k - 1 =", SSTR_df, "\n")
  cat("SSE =", SSE, "with df = = N - k =", SSE_df, "\n")
  MSSTR <- SSTR / SSTR_df
  cat("MSSTR =", MSSTR, "\n")
  MSSE <- SSE / SSE_df
  cat("MSSE =", MSSE, "\n")
  F <- MSSTR/MSSE
  cat("F = MSSTR/MSSE =", F, "\n")
  F_critical = qf(confidence, SSTR_df, SSE_df)
  cat("F_critical =", F_critical, "at", confidence, "confidence level with df1 =", SSTR_df, " and df2 =", SSE_df, "\n")
  if(F > F_critical) {
    cat("F > F_critical. The", nrow, "groups don't share the same mean.\n")
  } else {
    cat("F <= F_critical. The", nrow, "groups share the same mean.")
  }
} 

# linear regression

# y = B0 + B1*x
SSxx <- function(x) sum((x - mean(x))^2)
SSxy <- function(x,y) sum((x - mean(x))*(y - mean(y)))
B1 <- function(x,y) SSxy(x,y)/SSxx(x)
B0 <- function(x,y) mean(y) - B1(x,y)*mean(x)

# correlation measures whether 2 quantities share a linear relationship
# r = Pearson Correlation Coefficient
# |r| -> 1 means strong linear corelation
# |r| -> 0 means weak linear correlation
# when r > 0, x and y are positively corelated, ie. y increases with x.
# when r < 0, x and y are negatively corelated, ie. y decreases with x.

# cov(x,y) = E(XY) - E(X)E(Y)
# var(x) = E(X^2) - E(X)E(X)
# here are 2 ways of calculating the person corelation coefficient
pearson1 <- function(x,y) {
  numerator <- cov(x,y)
  denominator <- sqrt(var(x)*var(y))
  r <- numerator/denominator
  cat("pearson correlation coefficient =", r, "\n")
  return(r)
}

pearson2 <- function(n, sum_x, sum_x2, sum_y, sum_y2, sum_xy) {
  numerator <- n*sum_xy - sum_x*sum_y
  denominator <- sqrt(n*sum_x2 - sum_x^2)*sqrt(n*sum_y2 - sum_y^2)
  r <- numerator/denominator
  cat("pearson correlation coefficient =", r, "\n")
  return(r)
}

spearman1 <- function(x,y) {
  rx <- rank(x)
  ry <- rank(y)
  table <- rbind(x, rx, y, ry)
  print(table)
  n <- length(x)
  sum_rx <- sum(rx)
  sum_rx2 <- sum(rx^2)
  cat("sum_rx =", sum_rx, "  sum_rx2 =", sum_rx2, "\n")
  sum_ry <- sum(ry)
  sum_ry2 <- sum(ry^2)
  cat("sum_ry =", sum_ry, "  sum_ry2 =", sum_ry2, "\n")
  sum_rxry <- sum(rx*ry)
  cat("sum_rxry =", sum_rxry, "\n")
  numerator <- n*sum_rxry - sum_rx*sum_ry
  denominator <- sqrt(n*sum_rx2 - sum_rx^2)*sqrt(n*sum_ry2 - sum_ry^2)
  r <- numerator/denominator
  cat("spearman rank correlation coefficient = (n*sum_rxy - sum_rx*sum_ry) / (sqrt(n*sum_rx2 - sum_rx^2)*sqrt(n*sum_ry2 - sum_ry^2)) =", numerator, "/", denominator, "=", r, "\n")
  return(r)
}

spearman2 <- function(x,y) {
  rx = rank(x)
  ry = rank(y)
  n <- length(x)
  d = rx - ry
  table = data.frame(x, rx, y,  ry, d)
  print(table)
  sum_d2 = sum(d^2)
  r = 1 - 6*sum_d2/(n^3 - n)
  cat("n = ", n, "\nsum_d2 =", sum_d2, "\n")
  cat("spearman rank correlation coefficient =", "1 - 6*sum_d2/(n^3 - n) = ", r, "\n")
  return(r)
}

# chi-square test for independence
rowmatrix <- function(nrow, ncol, ...) {
  rows = list(...)
  n = nrow * ncol
  m = matrix(1:n,nrow,ncol)
  i = 1
  for (row in rows) {
    j = 1
    for(element in row) {
      m[i,j] = element
      j = j + 1
    }
    i = i + 1
  }
  return(m)
} 

ChiSq.Independence <- function(nrow, ncol, observed, confidence) {
  rows <- NULL
  for(i in 1:nrow) {
    rows <- append(rows, sum(observed[i,]))
  }
  N = sum(rows)
  rows = rowmatrix(1,nrow,rows)
  cols <- NULL
  for (j in 1:ncol) {
    cols <- append(cols, sum(observed[,j]))
  }
  cols = rowmatrix(1,ncol,cols)
  cat("N =", N, "\n")
  cat("table for row_count: cell(1, i) = row_count(i)\n")
  print(rows)
  cat("\ntable for col_count: cell(1, j) = col_count(j)\n")
  print(cols)
  
  expected <- observed
  for(i in 1:nrow) {
    for(j in 1:ncol) {
      expected[i,j] = rows[1,i]*cols[1,j]/N
    }
  }
  
  partial <- (observed - expected)^2/expected
  chi2 <- sum(partial)
  df = (nrow - 1)*(ncol - 1)
  chi2_critical <- qchisq(confidence, df)
  
  cat("\ntable for observed: cell(i,j) = O(i,j)\n")
  print(observed)
  cat("\ntable for expected: cell(i,j) = E(i,j) = row_count(i)*col_count(j)/N\n")
  print(expected)
  cat("\ntable for partial chi-square: cell(i,j) = (O(i,j) - E(i,j))^2/E(i,j)\n")
  print(partial)
  
  cat("\nchi-square =", chi2, "\n")
  cat("at", confidence, "confidence level with df =", df, ", chi-square_critical =", chi2_critical, "\n")
  if(chi2 <= chi2_critical) {
    cat("chi2 <= chi2_critical. There is insufficient evidence to reject that the categorical variables are independent.\n")
  } else {
    cat("chi2 > chi2_critical. There is sufficient evidence that the categorical variables are not independent.\n")
  }
}

ChiSq.DataFrame <- function(x, observation) {
  return(data.frame(x=x, observed=observation))
}

ChiSq.ToFitBinomial <- function(df, n, confidence) {
  # calculate MLE of p for binomial distribution
  p <- sum(df$x*df$observed)/(n*sum(df$observed))
  total <- sum(df$x)
  df$prob <- dbinom(df$x, n, p)
  df$expected <- df$prob * total
  df$chi2 <- (df$expected - df$observed)^2 / df$expected
  print(df)
  test <- sum(df$chi2)
  cat("test statistic =", test, "\n")
  chi2_critical <- qchisq(confidence,k-2)
  cat("at", confidence, "level, chi2_critical =", chi2_critical, "with df = k - p - 1 =", k-2, "\n")
  if(test > chi2_critical) {
    cat("test > chi2_critical: Binomial Model is not a good fit.\n")
  } else {
    cat("test <= chi2_critical: Bionomial Model is a good fit.\n")
  }
}

ChiSq.ToFitGeometric <- function(x, p) {
  
}

ChiSq.ToFitPoisson <- function(x, lambda) {
  
}

ChiSq.ToFitExpoenential <- function(x, lambda) {
  
}


