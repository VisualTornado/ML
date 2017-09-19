#!/usr/bin/env Rscript

#-----Import the Dataset-----#
getwd() # check current working directory

dataset <- read.csv('Data.csv')

#(dataset)

# Taking care of missing values

#----Calulate mean of the col seprately and apply a function using this mean including the missing values----#

dataset$Age <- ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)

dataset$Salary <- ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary)

#(dataset)

# Encoding categorical data

dataset$Country <- factor(dataset$Country, levels = c('France', 'Germany', 'Spain'), labels = c(1, 2, 3)) # Assigning factors to categorical text data using labels

dataset$Purchase <- factor(dataset$Purchase, levels = c('No', 'Yes'), labels = c(0, 1))                   # Assigning factors to categorical text data using labels

(dataset)

# Splitting Data in Traning and Test sets
#install.packages('caTools')
library(caTools)

set.seed('123')
split <- sample.split(dataset$Purchased, SplitRatio = 0.8)  # Dependent Variable, training set size, o/p is TRUE FALSE around which data is split.
training_set <- subset(dataset, split == TRUE)              
test_set <- subset(dataset, split == FALSE)

#(training_set)
#(test_set)

# Scaling

#training_set <- scale(training_set)  ==> These 2 would fail as in R factors are not numbers and for scaling we need only numeric values so col 1 and 4 are text/string.
#test_set <- scale(test_set)

training_set[,2:3] <- scale(training_set[,2:3])
test_set[,2:3] <- scale(test_set[,2:3])

(training_set)
(test_set)

""" NOTE: Dummy variables like binary values of country(Encoding categorical data) may or may not be NORMALIZED depending on the senario.
        Standardization = [(x-mean(x))/sd(x)]
        Normalization = [(x-min(x))/(max(x) - min(x))]"""
