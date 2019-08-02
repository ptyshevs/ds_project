# Import CSV file with preprocessed data*
csv <- read.csv("transformed_v2.csv")
head(csv)

# Install required packages
install.packages("party")
library("party")

set.seed(290875)
salary.cf <- cforest(salary ~ ., data = csv, control = cforest_unbiased(mtry = 2, ntree = 10))

# Standard importance
varimp(salary.cf)
