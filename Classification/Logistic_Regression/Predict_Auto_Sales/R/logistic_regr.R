# Logistic Regression

# Import the dataset
dataset = read.csv('Social_Network_Ads.csv')
dataset = dataset[, 3:5]

# Splitting data to training and test set
library('caTools')

set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == True)
test_set = subset(dataset, split == False)

# Feature Scaling

training_set = scale[training_set[, 3:5]]
test_set = scale[test_set[, 3:5]]

# Fitting the Logistic regression in training set

classifier = glm(Purchased ~ ., family = binomial, data = dataset)

print(classifier)

# Predicting the test set results

prob_pred = predict(classifier, type = 'response', newdata = test_se[-3])
y_pred = ifelse(prob_pred > 0.5, 1, 0)

print(y_pred)
