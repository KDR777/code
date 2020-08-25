This assignment asks you to examine the logistic regression for classification.
This dataset includes data on 200 cases:  maturity.csv

The data includes the following information:
	•	Mat: Maturity index 1~6 (Matured)
	•	Type: Type of School (Private=1/Public=0)
	•	Admit: (Admitted = 1, Otherwise 0)
Start by partitioning the data randomly into training and testing sets using a 6:4 ratio. Use the training set to fit a model and the testing set to assess the model performance. Consider a simple binary logistic model with Mat and Type predictors. This is analogous to the multiple regression model we learned in a statistical course.
Construct a logistic model for classification of the admission for graduate school using Mat and Type. After estimating the parameters using the training set, evaluate the model’s performance using the testing set.




data <- read.csv('/Users/kris/Documents/maturity.csv')
head(data)
str(data) # 199 obs, 3 vars. all integers. 
table(data$Maturity) # Target Variable? 1-6
table(data$Type) # 0s and 1s; 1=Private, 0= Public, 82 Public, 117 Private
table(data$Admit) #0s and 1s: 1 = Admitted, 0=Otherwise, 58 Admitted, 141 Otherwise.

# Convert 'Type' to 'Private' and 'Public':
#data$Type<- ifelse(data$Type=='1', 'Private', 'Public')

# Convert 'Admit' to 'Admitted' and 'Otherwise':
#data$Admit<- ifelse(data$Admit=='1', 'Admitted', 'Otherwise')



# Convert 'Type' and 'Admit' to factors:
data$Type<-as.factor(data$Type)
data$Admit<-as.factor(data$Admit)

# Verify the variables were converted to factors:
str(data)

# Partition data into training and testing 6:4 ratio:
library(caret)
set.seed(123)

#Target Variable: 'Admit'
Partition<-sample(c(1:dim(data)[1]), dim(data)[1]*0.6)
Train <- data[Partition, ]
Test <- data[-Partition, ]
str(Train) # 119 obs
str(Test) # 80 obs

# *Create Model* w/ LOGISTIC REGRESSION w/ glm() and *Training* data: 
myLogit <- glm(Admit~Maturity+Type, data = Train, family="binomial")
options(scipen=999)
summary(myLogit) 
# EQUATION of Estimation Functon: logit(p) = -8.4251+1.7030Maturity+2.1005Type
# We can now use this equation to plug-in the existing numbers from our dataset to determine the classification. 
head(data)
# If we take the first observation set: Maturity =1, Type= 1, and Admit= 1:
# logit(p) = -8.4251+1.7030*1+2.1005*1
# logit(p) = -8.4251 +1.7030+2.1005 
# logit(p) = -4.6216


# *Prediction function* for 'Admit' w/ use of Logistic Regression and *Test* data.
myLogitPred<- predict(myLogit, Test[, -3], type="response")

class(Test$Admit) # Factor
class(myLogitPred) #Numberic



# Confusion Matrix to compare prediction to actual:
confusionMatrix(as.factor(as.numeric(myLogitPred>0.5,1,0)), Test$Admit)

# Results: 87.5 percent accuracy. Correctly predicted 70/80. 
# The prediction model showed 51 would not be admitted and accuratly predected all for that catergory,
# but only accurately predicted 19 out othe 29 that would be admitted, meaning we have an 87.5% 
# accurate prediction model. 

















