# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 0.66)   # Remember R splitRatio is for training_set.
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

training_set
test_set

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

